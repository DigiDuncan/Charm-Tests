from typing import Literal
import arcade

from charm.lib.anim import ease_quartout
from charm.lib.charm import CharmColors, generate_gum_wrapper, move_gum_wrapper
from charm.lib.digiview import DigiView, ignore_imgui, shows_errors
from charm.lib.errors import TestError
from charm.lib.keymap import get_keymap
from charm.lib.settings import settings
from charm.objects.menu import MainMenu, MainMenuItem
from charm.views.cycletest import CycleView
from charm.views.emojitest import EmojiView
from charm.views.fnfsongmenu import FNFSongMenuView
from charm.views.fourkeysongmenu import FourKeySongMenuView
from charm.views.herotest import HeroTestView
from charm.views.newmenuview import NewMenuView
from charm.views.parallaxtest import ParallaxView
from charm.views.spritetest import SpriteTestView
from charm.views.taikotest import TaikoSongView
from charm.views.visualizer import VisualizerView
from charm.views.perspectivetest import PerspectiveView


class MainMenuView(DigiView):
    def __init__(self, back: DigiView):
        super().__init__(fade_in=1, bg_color=CharmColors.FADED_GREEN, back=back)

    def setup(self) -> None:
        super().setup()

        # Generate "gum wrapper" background
        self.logo_width, self.small_logos_forward, self.small_logos_backward = generate_gum_wrapper(self.size)

        self.menu = MainMenu([
            MainMenuItem("Playlists", "playlists", None),
            MainMenuItem("FNF Songs", "songs", FNFSongMenuView(back=self)),
            MainMenuItem("4K Songs", "songs", FourKeySongMenuView(back=self)),
            MainMenuItem("Options", "options", None),
            MainMenuItem("Emoji Test", "test", EmojiView(back=self)),
            MainMenuItem("Menu Test", "test", NewMenuView(back=self)),
            MainMenuItem("Cycler Test", "test", CycleView(back=self)),
            MainMenuItem("Sprite Test", "test", SpriteTestView(back=self)),
            MainMenuItem("Parallax Test", "test", ParallaxView(back=self)),
            MainMenuItem("Hero Test", "test", HeroTestView(back=self)),
            MainMenuItem("Perspective Test", "test", PerspectiveView(back=self)),
            MainMenuItem("Taiko Test", "test", TaikoSongView(back=self)),
            MainMenuItem("Scott Test", "test", VisualizerView(back=self))
        ])

        self.window.current_rp_state = "In Menus"
        self.window.update_rp("In Menus")

        self.load_countdown = None

    @shows_errors
    @ignore_imgui
    def on_key_press(self, symbol: int, modifiers: int) -> None:
        keymap = get_keymap()
        if symbol == arcade.key.RIGHT:
            self.menu.selected_id += 1
        elif symbol == arcade.key.LEFT:
            self.menu.selected_id -= 1
        elif symbol == keymap.back:
            self.back.setup()
            self.window.show_view(self.back)
            arcade.play_sound(self.window.sounds["back"], volume = settings.get_volume("sound"))
        elif symbol == keymap.start:
            if self.menu.selected.goto is not None:
                self.menu.loading = True
                self.load_countdown = 3  # Pause for three frames before loading. Ensure the text draws.
            else:
                self.menu.selected.jiggle_start = self.local_time
        elif symbol == arcade.key.E:
            raise TestError("You hit the E button! Don't do that.")
        elif symbol == arcade.key.F24:
            raise TestError("F24, let's go!")
        super().on_key_press(symbol, modifiers)

    @shows_errors
    @ignore_imgui
    def on_mouse_scroll(self, x: int, y: int, scroll_x: int, scroll_y: int) -> None:
        self.menu.selected_id += int(scroll_y)
        arcade.play_sound(self.window.sounds["select"])

    @shows_errors
    @ignore_imgui
    def on_mouse_press(self, x: float, y: float, button: int, modifiers: int) -> None:
        if button == arcade.MOUSE_BUTTON_LEFT:
            for item in self.menu.items:
                if item.collides_with_point((x, y)):
                    if item.go():
                        break
            else:
                self.menu.selected.jiggle_start = self.local_time

    @shows_errors
    def on_resize(self, width: int, height: int) -> None:
        self.menu.recreate()
        super().on_resize(width, height)

    @shows_errors
    def on_update(self, delta_time: float) -> None:
        super().on_update(delta_time)

        move_gum_wrapper(self.logo_width, self.small_logos_forward, self.small_logos_backward, delta_time)
        self.menu.on_update(delta_time)
        self.countdown()

    def countdown(self) -> None:
        if self.load_countdown is not None:
            self.load_countdown -= 1
        if self.load_countdown == 0:
            self.load_countdown = None
            self.menu.selected.go()

    @shows_errors
    def on_draw(self) -> None:
        self.window.camera.use()
        self.clear()

        # Charm BG
        self.small_logos_forward.draw()
        self.small_logos_backward.draw()

        left = ease_quartout(self.size[0], 0, 0.5, 1.5, self.local_time)
        arcade.draw_lrbt_rectangle_filled(left, self.size[0], self.size[1] // 4, (self.size[1] // 4) * 3, arcade.color.WHITE[:3] + (127,))

        self.menu.draw()

        super().on_draw()
