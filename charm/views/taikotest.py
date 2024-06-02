import logging
from math import ceil

import arcade
from charm.lib import paths

from charm.lib.charm import CharmColors, generate_gum_wrapper, move_gum_wrapper
from charm.lib.digiview import DigiView, ignore_imgui, shows_errors
from charm.lib.errors import NoChartsError
from charm.lib.gamemodes.four_key import FourKeyEngine
from charm.lib.gamemodes.taiko import TaikoHighway, TaikoSong
from charm.lib.keymap import keymap
from charm.lib.logsection import LogSection
from charm.lib.oggsound import OGGSound
from charm.lib.trackcollection import TrackCollection
from charm.views.resultsview import ResultsView
from charm.lib.keymap import keymap

logger = logging.getLogger("charm")


class TaikoSongView(DigiView):
    def __init__(self, back: DigiView):
        super().__init__(fade_in=1, bg_color=CharmColors.FADED_GREEN, back=back)
        self.name = "Freedom Dive"
        self.song_path = paths.songspath / "osu" / self.name
        self.tracks: TrackCollection = None
        self.highway: TaikoHighway = None
        self.engine: FourKeyEngine = None
        self.countdown: float = 3
        self.countdown_over = False

    @shows_errors
    def setup(self) -> None:
        with LogSection(logger, "loading audio"):
            audio_paths = [a for a in self.song_path.glob("*.mp3")] + [a for a in self.song_path.glob("*.wav")] + [a for a in self.song_path.glob("*.ogg")]
            trackfiles = []
            for s in audio_paths:
                trackfiles.append(OGGSound(s) if s.suffix == ".ogg" else arcade.Sound(s))
            self.tracks = TrackCollection([arcade.Sound(s) for s in audio_paths])

        with LogSection(logger, "loading song data"):
            self.taiko_song = TaikoSong.parse(self.song_path)
            self.chart = self.taiko_song.charts[0]
            if self.chart is None:
                raise NoChartsError(self.taiko_song.metadata.title)

        with LogSection(logger, "loading highway"):
            self.highway = TaikoHighway(self.chart, (0, self.window.height / 2), (self.window.width, 100), auto = True)

        self.text = arcade.Text("[LOADING]", -5, self.window.height - 5, color = arcade.color.BLACK, font_size = 24, align = "right", anchor_y="top", font_name = "bananaslip plus", width = self.window.width, multiline = True)
        self.countdown_text = arcade.Text("0", self.window.width / 2, self.window.height / 2, arcade.color.BLACK, 72, align="center", anchor_x="center", anchor_y="center", font_name = "bananaslip plus", width = 100)

        self.window.update_rp("Playing Taiko")

        # Generate "gum wrapper" background
        self.logo_width, self.small_logos_forward, self.small_logos_backward = generate_gum_wrapper(self.size)
        super().setup()
        self.success = True

    @shows_errors
    def on_show_view(self) -> None:
        self.window.theme_song.volume = 0
        if self.success is False:
            self.window.show_view(self.back)
            self.window.theme_song.volume = 0.25
        self.countdown = 4
        super().on_show_view()

    @shows_errors
    def on_key_something(self, symbol: int, modifiers: int, press: bool) -> None:
        pass

    def generate_data_string(self) -> str:
        return (f"Time: {int(self.tracks.time // 60)}:{int(self.tracks.time % 60):02}")

    @shows_errors
    @ignore_imgui
    def on_key_press(self, symbol: int, modifiers: int) -> None:
        super().on_key_press(symbol, modifiers)
        if keymap.back.pressed:
            self.go_back()
        elif keymap.pause.pressed:
            if self.countdown <= 0:
                self.tracks.pause() if self.tracks.playing else self.tracks.play()
        elif keymap.seek_zero.pressed:
            self.tracks.seek(0)
        elif keymap.seek_backward.pressed:
            self.tracks.seek(self.tracks.time - 5)
        elif keymap.seek_forward.pressed:
            self.tracks.seek(self.tracks.time + 5)
        elif self.window.debug and keymap.debug_toggle_hit_window:
            self.highway.show_hit_window = not self.highway.show_hit_window
        elif self.window.debug and keymap.debug_show_results:
            self.show_results()
        self.on_key_something(symbol, modifiers, True)

    @shows_errors
    def on_key_release(self, symbol: int, modifiers: int) -> None:
        super().on_key_release(symbol, modifiers)
        self.on_key_something(symbol, modifiers, False)

    def go_back(self) -> None:
        self.tracks.close()
        super().go_back()

    def show_results(self) -> None:
        self.tracks.close()
        results_view = ResultsView(self.engine.generate_results(), back = self.back)
        results_view.setup()
        self.window.show_view(results_view)

    def calculate_positions(self) -> None:
        self.highway.pos = (0, 0)
        self.highway.y += self.window.height // 2 - self.highway.h // 2  # center the highway
        self.text.position = (-5, self.window.height - 5)
        self.countdown_text.position = (self.window.width / 2, self.window.height / 2)
        super().calculate_positions()

    @shows_errors
    def on_update(self, delta_time) -> None:
        super().on_update(delta_time)

        if not self.tracks.loaded:
            return

        self.highway.update(0 - self.countdown if not self.countdown_over else self.tracks.time)

        data_string = self.generate_data_string()
        if self.text.text != data_string:
            self.text.text = data_string

        if self.countdown > 0:
            self.countdown -= delta_time
            if self.countdown < 0:
                self.countdown = 0
            self.countdown_text.text = str(ceil(self.countdown))

        if self.countdown <= 0 and not self.countdown_over:
            self.tracks.play()
            self.countdown_over = True

        if self.tracks.time >= self.tracks.duration:
            self.show_results()

        move_gum_wrapper(self.logo_width, self.small_logos_forward, self.small_logos_backward, delta_time)

    @shows_errors
    def on_draw(self) -> None:
        self.window.camera.use()
        self.clear()

        # Charm BG
        self.small_logos_forward.draw()
        self.small_logos_backward.draw()

        self.highway.draw()

        self.text.draw()

        if self.countdown > 0:
            self.countdown_text.draw()

        super().on_draw()
