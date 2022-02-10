import importlib.resources as pkg_resources
import logging
import statistics

import arcade
from digiformatter import logger as digilogger

import charm
import charm.data.images
from charm.lib.settings import Settings
from charm.lib.utils import pyglet_img_from_resource
from charm.objects.debug_log import DebugLog, PygletHandler

from .views.title import TitleView

SCREEN_WIDTH = Settings.width
SCREEN_HEIGHT = Settings.height
FPS_CAP = Settings.fps
SCREEN_TITLE = "Charm"

# Set up logging
logging.basicConfig(level=logging.INFO)
dfhandler = digilogger.DigiFormatterHandler()
dfhandlersource = digilogger.DigiFormatterHandler(showsource=True)
phandler = PygletHandler()
phandlersource = PygletHandler(showsource=True)

logger = logging.getLogger("charm")
logger.setLevel(logging.DEBUG)
logger.handlers = []
logger.propagate = False
logger.addHandler(dfhandler)
logger.addHandler(phandler)

arcadelogger = logging.getLogger("arcade")
arcadelogger.setLevel(logging.WARN)
arcadelogger.handlers = []
arcadelogger.propagate = False
arcadelogger.addHandler(dfhandlersource)
arcadelogger.addHandler(phandlersource)


class CharmGame(arcade.Window):
    def __init__(self):
        super().__init__(SCREEN_WIDTH, SCREEN_HEIGHT, SCREEN_TITLE, update_rate=1 / FPS_CAP)
        icon = pyglet_img_from_resource(charm.data.images, "charm-icon32t.png")
        self.set_icon(icon)

        self.delta_time = 0.0
        self.time = 0.0
        self.fps_checks = 0
        self.debug = False
        self.show_fps = True
        self.show_log = False
        self.sounds: dict[str, arcade.Sound] = {}
        self.theme_song: arcade.pyglet.media.Player = None

        self.fps_averages = []

        arcade.draw_text("abc", 0, 0)  # force font init

        self.debug_camera = arcade.Camera(SCREEN_WIDTH, SCREEN_HEIGHT)
        self.fps_label = arcade.pyglet.text.Label("???.? FPS",
                          font_name='bananaslip plus plus',
                          font_size=12,
                          x=0, y=self.height,
                          anchor_x='left', anchor_y='top',
                          color=(0, 0, 0) + (0xFF,))
        self.fps_shadow_label = arcade.pyglet.text.Label("???.? FPS",
                          font_name='bananaslip plus plus',
                          font_size=12,
                          x=1, y=self.height - 1,
                          anchor_x='left', anchor_y='top',
                          color=(0xAA, 0xAA, 0xAA) + (0xFF,))
        self.more_info_label = arcade.pyglet.text.Label("DEBUG",
                          font_name='bananaslip plus plus',
                          font_size=12,
                          x=0, y=self.height - self.fps_label.content_height - 5, multiline=True, width=Settings.width,
                          anchor_x='left', anchor_y='top',
                          color=(0, 0, 0) + (0xFF,))
        self.alpha_label = arcade.pyglet.text.Label("ALPHA",
                          font_name='bananaslip plus plus',
                          font_size=16,
                          x=self.width - 5, y=5,
                          anchor_x='right', anchor_y='bottom',
                          color=(0, 0, 0) + (32,))

        self.debug_log = DebugLog()
        self.log = self.debug_log.layout
        self.log.position = (5, 5)

        # Menu sounds
        for soundname in ["back", "select", "valid"]:
            with pkg_resources.path(charm.data.audio, f"sfx-{soundname}.wav") as p:
                self.sounds[soundname] = arcade.load_sound(p)

        self.title_view = TitleView()

    def setup(self):
        self.title_view.setup()
        self.show_view(self.title_view)

    def update(self, delta_time: float):
        self.delta_time = delta_time
        self.time += delta_time

    def debug_draw(self):
        self.fps_checks += 1
        _cam = self.current_camera
        self.debug_camera.use()
        if self.fps_checks % (FPS_CAP / 8) == 0:
            average = statistics.mean(self.fps_averages)
            self.fps_label.color = arcade.color.BLACK + (0xFF,) if average >= 120 else arcade.color.RED + (0xFF,)
            self.fps_label.text = self.fps_shadow_label.text = f"{average:.1f} FPS"
            self.fps_averages.clear()
        else:
            self.fps_averages.append(1 / self.delta_time)
        with self.ctx.pyglet_rendering():
            if self.show_fps or self.debug:
                self.fps_shadow_label.draw()
                self.fps_label.draw()
            if self.debug:
                self.more_info_label.draw()
                if self.show_log:
                    self.log.draw()
            self.alpha_label.draw()
        if _cam is not None:
            _cam.use()


def main():
    window = CharmGame()
    window.setup()
    arcade.run()


if __name__ == "__main__":
    main()