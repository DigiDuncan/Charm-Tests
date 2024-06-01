from collections import deque
import logging
import random
import statistics
import typing
from typing import TypedDict
import importlib.resources as pkg_resources

import arcade
import pyglet
from pyglet.media import Player
import pypresence
import imgui
from imgui.integrations.pyglet import create_renderer

from charm.lib import debug_menu
from charm.lib.anim import ease_expoout
from charm.lib.bpmanim import BPMAnimator
from charm.lib.errors import CharmException
from charm.lib.generic.song import BPMChangeEvent
import charm.data.audio

logger = logging.getLogger("charm")

rpc_client_id = "1056710104348639305"  # Charm app on Discord.

if typing.TYPE_CHECKING:
    from charm.lib.digiview import DigiView


class Eggs:
    TRICKY = 666


class DebugSettings(TypedDict):
    show_fps: bool


class DigiWindow(arcade.Window):
    def __init__(self, size: tuple[int, int], title: str, fps_cap: int, initial_view: DigiView):
        super().__init__(size[0], size[1], title, update_rate=1 / fps_cap, enable_polling=True, resizable=True)

        self.fps_cap = fps_cap
        self.initial_view = initial_view

        self.delta_time = 0.0
        self.time = 0.0
        self.fps_checks = 0
        self.debug = False
        self.sounds: dict[str, arcade.Sound] = {}

        # Play music
        with pkg_resources.path(charm.data.audio, "song.mp3") as p:
            song = arcade.Sound(p)
        theme_song: Player | None = arcade.play_sound(song, 0, loop=True)
        if theme_song is None:
            raise CharmException("Song Failed", "Failed to load theme song")
        self.theme_song = theme_song

        self.bpm_events = [BPMChangeEvent(0, 120), BPMChangeEvent(3, 220)]
        self.beat_animator = BPMAnimator(self.bpm_events, ease_expoout)

        # Discord RP
        try:
            self.rpc = pypresence.Presence(rpc_client_id)
        except pypresence.DiscordNotFound:
            self.rpc = None
        self.rpc_connected = False
        self.last_rp_time = 0
        self.current_rp_state = ":jiggycat:"
        self._rp_stale = True
        if self.rpc:
            try:
                self.rpc.connect()
                self.rpc_connected = True
            except pypresence.DiscordError:
                logger.warn("Discord could not connect the rich presence.")
        else:
            logger.warn("Couldn't make a Discord RPC object!")

        self.fps_averages: list[float] = []

        arcade.draw_text(" ", 0, 0)  # force font init (fixes lag on first text draw)

        # Cameras and text labels
        self.camera = arcade.camera.Camera2D()
        self.overlay_camera = arcade.camera.Camera2D()
        self.fps_label = pyglet.text.Label("???.? FPS",
                                           font_name='bananaslip plus',
                                           font_size=12,
                                           x=0, y=self.height,
                                           anchor_x='left', anchor_y='top',
                                           color=(0, 0, 0, 0xFF))
        self.fps_shadow_label = pyglet.text.Label("???.? FPS",
                                                  font_name='bananaslip plus',
                                                  font_size=12,
                                                  x=1, y=self.height - 1,
                                                  anchor_x='left', anchor_y='top',
                                                  color=(0xAA, 0xAA, 0xAA, 0xFF))
        self.more_info_label = pyglet.text.Label("DEBUG",
                                                 font_name='bananaslip plus',
                                                 font_size=12,
                                                 x=0, y=self.height - self.fps_label.content_height - 5,
                                                 multiline=True, width=self.width,
                                                 anchor_x='left', anchor_y='top',
                                                 color=(0, 0, 0, 0xFF))
        self.alpha_label = pyglet.text.Label("ALPHA",
                                             font_name='bananaslip plus',
                                             font_size=16,
                                             x=self.width - 5, y=5,
                                             anchor_x='right', anchor_y='bottom',
                                             color=(0, 0, 0, 32))

        # Debug menu
        imgui.create_context()
        imgui.get_io().display_size = 100, 100
        imgui.get_io().fonts.get_tex_data_as_rgba32()
        self.impl = create_renderer(self)
        self.fps_list = deque[float]()
        self.beat_list = deque[float]()
        self.debug_settings: DebugSettings = {
            "show_fps": False
        }

        # Egg roll
        self.egg_roll = random.randint(1, 1000)

    def setup(self) -> None:
        self.initial_view.setup()
        self.show_view(self.initial_view)
        self.update_rp()

    def on_update(self, delta_time: float) -> None:
        self.delta_time = delta_time
        self.time += delta_time
        self.update_rp()
        self.beat_animator.update(self.theme_song.time)

    def on_resize(self, width: int, height: int) -> None:
        super().on_resize(width, height)

        self.overlay_camera.match_screen(and_projection=True)
        self.overlay_camera.position = self.center

        self.fps_label.position = (0, self.height, 0)
        self.fps_shadow_label.position = (1, self.height - 1, 0)
        self.more_info_label.position = (0, self.height - self.fps_label.content_height - 5, 0)
        self.alpha_label.position = (self.width - 5, 5, 0)

    def update_rp(self, new_state: str | None = None) -> None:
        if self.rpc is None or not self.rpc_connected:
            return
        if new_state and self.current_rp_state != new_state:
            self.current_rp_state = new_state
            self._rp_stale = True
        if (self.last_rp_time + 1 < self.time) and self._rp_stale:
            self.rpc.update(state=self.current_rp_state,
                            large_image="charm-icon-square", large_text="Charm Logo")
            self.last_rp_time = self.time
            self._rp_stale = False

    def overlay_draw(self) -> None:
        self.fps_checks += 1
        _cam = self.current_camera
        self.overlay_camera.use()

        # FPS Counter
        if self.fps_checks % 30 == 0:
            average = statistics.mean(self.fps_averages)
            self.fps_label.color = arcade.color.BLACK if average >= 120 else arcade.color.RED
            self.fps_label.text = self.fps_shadow_label.text = f"{average:.1f} FPS"
            self.fps_averages.clear()
        else:
            self.fps_averages.append(1 / self.delta_time)

        # FPS Graph
        self.fps_list.append(1 / self.delta_time)
        if len(self.fps_list) > 240:
            self.fps_list.popleft()

        # Beat Graph
        self.beat_list.append(self.beat_animator.factor)
        if len(self.beat_list) > 240:
            self.beat_list.popleft()

        # Labels
        if self.debug_settings["show_fps"] or self.debug:
            self.fps_shadow_label.draw()
            self.fps_label.draw()
        if self.debug:
            self.more_info_label.draw()
        self.alpha_label.draw()

        # Debug menu
        if self.debug:
            debug_menu.draw(self)

        _cam.use()

    def save_atlas(self) -> None:
        self.ctx.default_atlas.save("atlas.png")
