from arcade import LRBT

from charm.lib.mini_mint import Element, VerticalElementList

from charm.ui.menu_list.song_element import SongListElement
from charm.ui.menu_list.song_stub import Song, Metadata, Chart

# -- TEMP --
from arcade import draw_text


class SongMenuListElement(Element[VerticalElementList]):

    def __init__(self, songs: list[Song] = None, min_element_size: float = 100, element_padding: int = 2, left_fraction: float = 0.0, right_fraction: float = 1.0):
        super().__init__()
        self.min_element_size: float = min_element_size  # uses this to estimate the number of needed elements to simulate the full list
        self.element_padding: int = element_padding  # uses this to make sure the full list illusion isn't broken

        self.left_fraction: float = left_fraction  # How far from the left side of the region to start the bounds.
        self.right_fraction: float = right_fraction  # How far from the left side of the region to end the bounds.

        self.songs: list[Song] = songs or []

        self.highlighted_song_idx: int = 0
        self.song_scroll: float = 0.0
        self.highlighted_chart_idx: int = 0
        self.chart_scroll: float = 0.0
        self.current_selected_song: Song = None
        self.current_selected_chart: Chart = None

        self.element_list: VerticalElementList[SongListElement] = VerticalElementList(strict=False)
        self.add_child(self.element_list)

        self.layout(force=True)

    def set_songs(self, songs: list[Song]) -> None:
        self.songs = songs
        self.highlighted_song_idx = 0
        self.highlighted_chart_idx = 0
        self.current_selected_song = None
        self.current_selected_chart = None
        self._initialise_song_elements()
        self.invalidate_layout()

    def _initialise_song_elements(self):
        self.element_list.empty()
        v = self.bounds.height
        vh = v / 2.0

        half_count = int(vh // self.min_element_size) + self.element_padding

        center = SongListElement(self.min_element_size)
        center.song = self.songs[0]
        self.element_list.add_child(center)

        for idx in range(half_count):
            above_element = SongListElement(self.min_element_size)
            self.element_list.insert_child(above_element, 0)
            post_element = SongListElement(self.min_element_size)
            if (idx + 1) < len(self.songs):
                post_element.song = self.songs[idx + 1]
            self.element_list.add_child(post_element)

    def _calc_layout(self) -> None:
        self.song_scroll = self.highlighted_song_idx

        v = self.bounds.height
        vh = v / 2.0

        half_count = int(vh // self.min_element_size) + self.element_padding
        v_count = half_count + 0.5
        top = self.bounds.y + v_count * self.min_element_size
        bot = self.bounds.y - v_count * self.min_element_size
        lef = self.bounds.left + self.left_fraction * self.bounds.width
        rig = self.bounds.left + self.right_fraction * self.bounds.width

        curr_count = len(self.element_list.children)
        child_count = int(v_count*2)
        if curr_count == 0:
            return

        _center_idx = int(self.song_scroll)
        _current_end_idx = _center_idx + half_count
        _current_start_idx = _center_idx - half_count

        # TODO: Find why the elements may be empty when they shouldn't be
        # TODO: Figure out a way to account for each elements size when idx scrolling

        if curr_count > child_count:
            for _ in range((curr_count - child_count) // 2):
                self.element_list.remove_child(self.element_list.children[0])
                self.element_list.remove_child(self.element_list.children[-1])
            # remove children
        elif curr_count < child_count:
            for idx_offset in range((child_count - curr_count) // 2):
                start_element = SongListElement(self.min_element_size)
                if 0 <= _current_start_idx - idx_offset < len(self.songs):
                    start_element.song = self.songs[_current_start_idx - idx_offset]
                self.element_list.insert_child(start_element, 0)
                end_element = SongListElement(self.min_element_size)
                if 0 <= _current_end_idx + idx_offset < len(self.songs):
                    end_element.song = self.songs[_current_end_idx + idx_offset]
                self.element_list.add_child(end_element)
            # add children

        # Idx scroll
        idx_offset = self.min_element_size * self.song_scroll

        # Sub scroll

        # The menu list works with the children's minimum size to figure out the needed offset
        centering_offset = sum(child.minimum_size.y for child in self.element_list.children[:half_count]) - (half_count * self.min_element_size)

        self.element_list.bounds = LRBT(lef, rig, bot + centering_offset + idx_offset, top + centering_offset + idx_offset)

    def _select_current_song(self):
        self.current_selected_song = self.songs[self.highlighted_song_idx]
        self.highlighted_chart_idx = 0

        #TODO: Open highlighted song element

    def _select_current_chart(self):
        self.current_selected_chart = self.current_selected_song.charts[self.highlighted_chart_idx]

        #TODO: load chart?

    def select(self):
        if self.current_selected_song is None:
            self._select_current_song()
            return
        self._select_current_chart()

    def _down_sub_scroll(self):
        self.highlighted_chart_idx += 1

        if self.highlighted_chart_idx < len(self.current_selected_song.charts):
            return

        # We are outside the chartsets list of charts, so lets close it
        self.current_selected_chart = None
        self.current_selected_song = None
        self.highlighted_chart_idx = 0
        # TODO: Toggle the current song element

        self._down_scroll()

    def _down_scroll(self):
        self.highlighted_song_idx = (self.highlighted_song_idx + 1) % len(self.songs)

    def down_scroll(self):
        if self.current_selected_song is not None:
            self._down_sub_scroll()
            return
        self._down_scroll()

    def _up_sub_scroll(self):
        self.highlighted_chart_idx -= 1

        if self.highlighted_chart_idx >= 0:
            return

        # We are outside the chartsets list of charts, so lets close it
        self.current_selected_chart = None
        self.current_selected_song = None
        self.highlighted_chart_idx = 0
        # TODO: Toggle the current song element

    def _up_scroll(self):
        self.highlighted_song_idx = (self.highlighted_song_idx - 1) % len(self.songs)

    def up_scroll(self):
        if self.current_selected_song is not None:
            self._up_sub_scroll()
            return
        self._up_scroll()

    def _display(self) -> None:
        draw_text(
            f'highlighted song: {self.highlighted_song_idx} - {self.songs[self.highlighted_song_idx]}',
            self.bounds.right - 5.0, self.bounds.y, anchor_x='right', color=(0, 0, 0, 255)#
        )
        draw_text(
            f'selected song: {self.current_selected_song}',
            self.bounds.right - 5.0, self.bounds.y - 15.0, anchor_x='right', color=(0, 0, 0, 255)
        )
        c_chart_idx = None if self.current_selected_song is None else self.highlighted_chart_idx
        c_chart = None if self.current_selected_song is None else self.current_selected_song.charts[self.highlighted_chart_idx]
        draw_text(
            f'highlighted chart: {c_chart_idx} - {c_chart}',
            self.bounds.right - 5.0, self.bounds.y - 30.0, anchor_x='right', color=(0, 0, 0, 255)
        )
        draw_text(
            f'selected chart: {self.current_selected_chart}',
            self.bounds.right - 5.0, self.bounds.y - 45.0, anchor_x='right', color=(0, 0, 0, 255)
        )
