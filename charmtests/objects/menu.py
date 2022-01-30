import io
import logging
import requests
import sys

import arcade
from arcade import Sprite
import PIL.Image

from charmtests.lib.anim import ease_circout
from charmtests.lib.settings import Settings
from charmtests.objects.song import Song

logger = logging.getLogger(__package__)


class MenuItem(Sprite):
    cid = 0

    def __init__(self, song: Song, w: int = None, h: int = None, *args, **kwargs):
        self.song = song
    
        self.title = song.title
        self.artist = song.artist
        self.album = song.album
        self.grade = song.grade
        self.length = song.length
        self.difficulty = song.difficulty
        self.best_score = song.best_score

        try:
            album_art_img = PIL.Image.open(f"./albums/album_{self.__class__.cid}.png")
        except FileNotFoundError:
            album_art = io.BytesIO(requests.get("https://picsum.photos/200.jpg").content)
            album_art_img = PIL.Image.open(album_art)
            album_art_img = album_art_img.convert("RGBA")
            album_art_img.save(f"./albums/album_{self.__class__.cid}.png")
        self.album_art = arcade.Texture(f"{self.__class__.__name__}-{self.__class__.cid}-albumart", album_art_img, hit_box_algorithm=None)

        self._w = w if w else Settings.width // 2
        self._h = h if h else Settings.height // 8

        self._tex = arcade.Texture.create_empty(f"{self.__class__.__name__}-{self.__class__.cid}", (self._w, self._h))
        self.__class__.cid += 1
        super().__init__(texture = self._tex, *args, **kwargs)
        self._sprite_list = arcade.SpriteList()
        self._sprite_list.append(self)

        self.position = (0, -Settings.height)

        with self._sprite_list.atlas.render_into(self._tex) as fbo:
            fbo.clear()
            arcade.draw_circle_filled(self.width - self.height / 2, self.height / 2, self.height / 2, arcade.color.WHITE)
            arcade.draw_lrtb_rectangle_filled(0, self.width - self.height / 2, self.height, 0, arcade.color.WHITE)
            arcade.draw_text(
                self.title, self.width - self.height / 2 - 5, self.height / 2, arcade.color.BLACK,
                font_size=self.height/3 * (3/4), font_name="bananaslip plus plus", anchor_x="right"
            )
            arcade.draw_text(
                self.artist + ", " + self.album, self.width - self.height / 2 - 5, self.height / 2, arcade.color.BLACK,
                font_size=self.height/4 * (3/4), font_name="bananaslip plus plus", anchor_x="right", anchor_y="top"
            )

        logger.info(f"Loaded MenuItem {self.title}")

class Menu:
    def __init__(self, songs: list[Song] = None, radius = 4, buffer = 5, move_speed = 2.5) -> None:
        self._songs = songs
        self.items: list[MenuItem] = []
        if songs:
            for song in self._songs:
                self.items.append(MenuItem(song))
        self.sprite_list = arcade.SpriteList()
        for item in self.items:
            self.sprite_list.append(item)

        self.buffer = buffer
        self.move_speed = move_speed
        self.radius = radius

        self._selected_id = 0

        self.local_time = 0
        self.move_start = sys.maxsize

    @property
    def selected_id(self) -> int:
        return self._selected_id

    @selected_id.setter
    def selected_id(self, v: int):
        self._selected_id = v
        self.move_start = self.local_time

    @property
    def selected(self) -> MenuItem:
        return self.items[self.selected_id]

    @property
    def move_end(self) -> float:
        return self.move_start + self.move_speed

    def sort(self, key: str, rev: bool = False):
        selected = self.items[self.selected_id]
        self.items.sort(key=lambda item: getattr(item.song, key), reverse=rev)
        self.selected_id = self.items.index(selected)

    def update(self, local_time: float):
        self.local_time = local_time
        old_pos = {}
        for item in self.items:
            old_pos[item] = (item.left, item.center_y)
        current = self.items[self.selected_id]
        current.left = ease_circout(old_pos[current][0], 0, self.move_start, self.move_end, self.local_time)
        current.center_y = ease_circout(old_pos[current][1], Settings.height // 2, self.move_start, self.move_end, self.local_time)
        up_id = self.selected_id
        down_id = self.selected_id
        x_delta = current.width / (self.radius + 1) / 1.5
        x_offset = 0
        y_offset = 0
        for i in range(self.radius + 1):
            up_id -= 1
            down_id += 1
            x_offset += x_delta
            y_offset += current.height + self.buffer
            if up_id > -1:
                up = self.items[up_id]
                up.left = ease_circout(old_pos[up][0], current.left - x_offset, self.move_start, self.move_end, self.local_time)
                up.center_y = ease_circout(old_pos[up][1], y_offset + current.center_y, self.move_start, self.move_end, self.local_time)
            if down_id < len(self.items):
                down = self.items[down_id]
                down.left = ease_circout(old_pos[down][0], current.left - x_offset, self.move_start, self.move_end, self.local_time)
                down.center_y = ease_circout(old_pos[down][1], -y_offset + current.center_y, self.move_start, self.move_end, self.local_time)

    def draw(self):
        self.sprite_list.draw()
