from math import fmod

from charm.lib.mini_mint import Element, VerticalElementList

from charm.ui.menu_list.chartset_element import ChartsetElement

from charm.game.generic import ChartSet, ChartMetadata, ChartSetMetadata

# -- TEMP --
from importlib.resources import files
from arcade import Text, draw_text, draw_rect_filled, XYWH, LBWH, LRBT, get_window, draw_texture_rect, Texture
from arcade.types import Color
from charm.lib.utils import get_font_size, img_from_path, kerning
import PIL.Image
import charm.data.images

# -- PROCEDURAL ANIMATION CONSTANTS --
CHARTSET_FREQUENCY = 2.0
CHARTSET_DAMPING = 0.8
CHARTSET_RESPONSE = 0.75
CHART_FREQUENCY = 2.0
CHART_DAMPING = 0.8
CHART_RESPONSE = 0.75


class UnifiedChartsetMenuElement(Element):
    def __init__(self, chartsets: list[ChartSet] | None = None, min_element_size: float = 100, element_padding: int = 2, left_fraction: float = 0.0, right_fraction: float = 1.0):
        super().__init__()
        self.min_element_size: float = min_element_size  # uses this to estimate the number of needed elements to simulate the full list
        self.element_padding: int = element_padding  # uses this to make sure the full list illusion isn't broken

        self.left_fraction: float = left_fraction  # How far from the left side of the region to start the bounds.
        self.right_fraction: float = right_fraction  # How far from the left side of the region to end the bounds.

        self.chartsets: list[ChartSet] = []

        self._highlighted_set_idx: int = 0
        self.set_scroll: float = 0.0
        self._highlighted_chart_idx: int = 0
        self.chart_scroll: float = 0.0
        self.current_selected_chartset: ChartSet | None = None
        self.current_selected_chart: ChartMetadata | None = None

        self.set_scroll_animation = Element.Animator.start_procedural_animation(
            self.update_set_scroll,
            self.highlighted_set_idx, 0.0,
            self.set_scroll, self.set_scroll, 0.0,
            CHARTSET_FREQUENCY, CHARTSET_DAMPING, CHARTSET_RESPONSE
        )
        self.chart_scroll_animation = Element.Animator.start_procedural_animation(
            self.update_chart_scroll,
            self.chart_scroll, 0.0,
            self.highlighted_chart_idx, self.highlighted_chart_idx, 0.0,
            CHART_FREQUENCY, CHART_DAMPING, CHART_RESPONSE
        )

        self.shown_sets: dict[ChartSetMetadata, ChartsetElement] = {}

        self.element_list: VerticalElementList = VerticalElementList(strict=False)
        self.add_child(self.element_list)

        if chartsets:
            self.set_chartsets(chartsets)

        self.layout(force=True)

        # -- TEMP --
        self.album_art_texture: Texture | None = None

    def set_chartsets(self, chartsets: list[ChartSet]) -> None:
        if len(self.chartsets) > len(chartsets):
            self.highlighted_set_idx = 0
            self.highlighted_chart_idx = 0

        self.chartsets = chartsets
        self.current_selected_chartset = None
        self.current_selected_chart = None
        self._place_chartset_elements()
        self.invalidate_layout()

    def _fetch_chartset_element(self, idx: int) -> ChartsetElement:
        """
        Create or get the chartset element for a given chartset index,
        for an idx outside the range of chartsets return a ChartsetElement with no chartset
        """
        element_set = None if (len(self.chartsets) <= idx or idx < 0) else self.chartsets[idx]
        element = None

        if element_set:
            element = self.shown_sets.get(element_set.metadata, None)

        if element is None:
            element = ChartsetElement(self.min_element_size, element_set)

        return element

    def _place_chartset_elements(self) -> None:
        self.element_list.empty()
        if not self.chartsets:
            return
        v = self.bounds.height
        vh = v / 2.0

        # The number of elements we need above the center element
        half_count = int(vh // self.min_element_size) + self.element_padding

        # The index of the center element
        start_idx = int(self.set_scroll)

        # A map from the chartset metadata to the element
        next_songs = {}

        # get the center element
        center = self._fetch_chartset_element(start_idx)

        if center.chartset is not None:
            next_songs[center.chartset.metadata] = center
            # If the chartset is selected lets open it
            if center.chartset == self.current_selected_chartset:
                center.select()
        self.element_list.add_child(center)

        # The half count doesn't include the center so we 'expand' outward finding
        # the chartsets and elements
        for offset in range(1, half_count + 1):
            # find the next chartset above the center
            above_idx = start_idx - offset
            above_element = self._fetch_chartset_element(above_idx)
            if above_element.chartset is not None:
                next_songs[above_element.chartset.metadata] = above_element
                if above_element.chartset == self.current_selected_chartset:
                    above_element.select()
            self.element_list.insert_child(above_element, 0)

            # find the next chartset below the center
            post_idx = start_idx + offset
            post_element = self._fetch_chartset_element(post_idx)
            if post_element.chartset is not None:
                next_songs[post_element.chartset.metadata] = post_element
                if post_element.chartset == self.current_selected_chartset:
                    post_element.select()
            self.element_list.add_child(post_element)

        self.shown_sets = next_songs

    def update_set_scroll(self, new_scroll: float, delta_scroll: float) -> None:
        self.set_scroll = new_scroll
        self.invalidate_layout()

    def update_chart_scroll(self, new_scroll: float, delta_scroll: float) -> None:
        self.chart_scroll = new_scroll
        self.invalidate_layout()

    def _calc_layout(self) -> None:
        v = self.bounds.height
        vh = v / 2.0

        half_count = int(vh // self.min_element_size) + self.element_padding
        v_count = half_count + 0.5
        top = self.bounds.y + v_count * self.min_element_size
        bot = self.bounds.y - v_count * self.min_element_size
        lef = self.bounds.left + self.left_fraction * self.bounds.width
        rig = self.bounds.left + self.right_fraction * self.bounds.width

        self._place_chartset_elements()

        # Idx scroll
        scroll_size = self.min_element_size if not self.element_list.children else self.element_list.children[half_count].minimum_size.y
        idx_scroll = fmod(self.set_scroll, 1.0) * scroll_size

        # Sub scroll
        if self.current_selected_chartset and self.current_selected_chartset.metadata in self.shown_sets and self.shown_sets[self.current_selected_chartset.metadata].list_element_children:
            element = self.shown_sets[self.current_selected_chartset.metadata]
            core = element.chartset_element_bounds.y
            target = element.list_element_children[self._highlighted_chart_idx].bounds.y
            self.chart_scroll_animation.target_x = (core - target)
        else:
            self.chart_scroll_animation.target_x = 0.0
        sub_scroll = self.chart_scroll
        # print(sub_scroll)

        # The menu list works with the children's minimum size to figure out the needed offset
        centering_offset = sum(child.minimum_size.y for child in self.element_list.children[:half_count]) - (half_count * self.min_element_size)

        self.element_list.bounds = LRBT(lef, rig, bot + centering_offset + sub_scroll + idx_scroll, top + centering_offset + sub_scroll + idx_scroll)

    @property
    def highlighted_set_idx(self) -> int:
        return self._highlighted_set_idx

    @highlighted_set_idx.setter
    def highlighted_set_idx(self, new_idx: int) -> None:
        self._highlighted_set_idx = new_idx
        self.set_scroll_animation.target_x = new_idx

    @property
    def highlighted_chart_idx(self) -> int:
        return self._highlighted_chart_idx

    @highlighted_chart_idx.setter
    def highlighted_chart_idx(self, new_idx: int) -> None:
        self._highlighted_chart_idx = new_idx

    def select_set(self, chartset: ChartSet) -> None:
        if self.current_selected_chartset is not None and self.current_selected_chartset.metadata in self.shown_sets:
            self.shown_sets[self.current_selected_chartset.metadata].deselect()

        self.current_selected_chartset = chartset
        self.highlighted_chart_idx = 0
        self.invalidate_layout()

        if chartset.metadata in self.shown_sets:
            self.shown_sets[chartset.metadata].select()
        #TODO: If the song element doesn't exist, delay the opening, or track that it needs to happen at creation

        if chartset.metadata.album_art:
            _img = PIL.Image.open(chartset.metadata.path / chartset.metadata.album_art)
        else:
            _img = img_from_path(files(charm.data.images) / "no_image_found.png")
        self.album_art_texture = Texture(_img)

    def deselect_set(self, chartset: ChartSet) -> None:
        if chartset != self.current_selected_chartset:
            return

        self.album_art_texture = None

        # We are outside the chartsets list of charts, so lets close it
        if self.current_selected_chartset is None:
            raise Exception("Really Bad Error")
        if self.current_selected_chartset.metadata in self.shown_sets:
            self.shown_sets[self.current_selected_chartset.metadata].deselect()
        self.current_selected_chartset = None
        self.current_selected_chart = None
        self.highlighted_chart_idx = 0

    def select_chart(self, chart: ChartMetadata) -> None:
        self.current_selected_chart = chart
        self.invalidate_layout()
        #TODO: load chart?

    def select_chart_element(self, element: ChartsetElement) -> None:
        print('not yet implemented internally')

    def select_currently_highlighted(self) -> None:
        self.invalidate_layout()
        if self.current_selected_chartset is None:
            self.select_set(self.chartsets[self.highlighted_set_idx])
            return
        self.select_chart(self.current_selected_chartset.charts[self.highlighted_chart_idx])

    def _down_sub_scroll(self, count: int) -> None:
        if self.current_selected_chartset is None:
            raise Exception("Really Bad Error")
        self.highlighted_chart_idx += count

        if self.highlighted_chart_idx < len(self.current_selected_chartset.charts):
            return

        self.deselect_set(self.current_selected_chartset)
        self._down_scroll(count=1)

    def _down_scroll(self, count: int) -> None:
        if not self.chartsets:
            return
        self.highlighted_set_idx = (self.highlighted_set_idx + count) % len(self.chartsets)

    def down_scroll(self, count: int = 1) -> None:
        self.invalidate_layout()
        if self.current_selected_chartset is not None:
            self._down_sub_scroll(count=count)
            return
        self._down_scroll(count=count)

    def _up_sub_scroll(self, count: int) -> None:
        if self.current_selected_chartset is None:
            raise Exception("Really Bad Error")
        self.highlighted_chart_idx -= count

        if self.highlighted_chart_idx >= 0:
            return

        # We are outside the chartsets list of charts, so lets close it
        self.deselect_set(self.current_selected_chartset)

    def _up_scroll(self, count: int) -> None:
        if not self.chartsets:
            return
        self.highlighted_set_idx = (self.highlighted_set_idx - count) % len(self.chartsets)

    def up_scroll(self, count: int = 1) -> None:
        self.invalidate_layout()
        if self.current_selected_chartset is not None:
            self._up_sub_scroll(count=count)
            return
        self._up_scroll(count=count)

    def _display(self) -> None:
        # If the highlighed chartset has an element on screen draw a small marker
        if self.chartsets[self.highlighted_set_idx].metadata in self.shown_sets:
            element = self.shown_sets[self.chartsets[self.highlighted_set_idx].metadata]
            draw_rect_filled(XYWH(element.chartset_element_bounds.right + 15, element.chartset_element_bounds.center_y, 12, 12), (255, 151, 135, 255))

        # If we haven't selected a chartset then we are done
        if self.current_selected_chartset is None:
            return

        ### DIGI: BEGIN METADATA DISPLAY HACK ###

        win = get_window()
        metadata = self.current_selected_chartset.metadata
        WIDTH = win.width
        HEIGHT = win.height
        ONE_THIRD_W = WIDTH / 3
        FIVE_SIXTH_W = WIDTH * (5 / 6)

        # Background
        draw_rect_filled(LBWH(ONE_THIRD_W * 2, 0, ONE_THIRD_W, HEIGHT), Color(0, 0, 0, 50))

        # Title | Artist | Album
        title_text = Text(metadata.title or "???", FIVE_SIXTH_W, win.center_y, anchor_x='center', color=(0, 0, 0, 255), font_name="bananaslip plus", font_size=get_font_size(metadata.title or "???", 24, ONE_THIRD_W))
        artist_text = Text(metadata.artist or "Unknown Artist", FIVE_SIXTH_W, win.center_y - 32, anchor_x='center', color=(0, 0, 0, 255), font_name="bananaslip plus", font_size=get_font_size(metadata.artist or "Unknown Artist", 16, ONE_THIRD_W))
        album_text = Text(metadata.album or "Unknown Album", FIVE_SIXTH_W, win.center_y - 64, anchor_x='center', color=(0, 0, 0, 255), font_name="bananaslip plus", font_size=get_font_size(metadata.album or "Unknown Album", 16, ONE_THIRD_W))

        # TODO | FONT: Remove once kerning in the font file is fixed!
        title_text._label.set_style("kerning", kerning(-120, 24))
        artist_text._label.set_style("kerning", kerning(-120, 16))
        album_text._label.set_style("kerning", kerning(-120, 16))

        title_text.draw()
        artist_text.draw()
        album_text.draw()

        # If source...
        if metadata.source:
            source_text = Text(f"from {metadata.source}", FIVE_SIXTH_W, win.center_y - 96, anchor_x='center', color=(0, 0, 0, 255), font_name="bananaslip plus", font_size=get_font_size(f"from {metadata.source}", 16, ONE_THIRD_W), italic = True)
            source_text._label.set_style("kerning", kerning(-120, 16))
            source_text.draw()

        # The worst way to get album art
        if self.album_art_texture is not None:
            draw_texture_rect(self.album_art_texture, XYWH(FIVE_SIXTH_W, win.center_y + 135, 200, 200))

        ### DIGI: END METADATA DISPLAY HACK ###

        # If the current chart set ins't on screen we are done
        if self.current_selected_chartset.metadata not in self.shown_sets:
            return

        # try to mark the currently highlighted chart within the chartset.
        # For the first frame after being selected the sub elements may not exsist so we catch that error and ignore it.
        try:
            element = self.shown_sets[self.current_selected_chartset.metadata].get_chart_element_from_idx(self.highlighted_chart_idx)
            draw_rect_filled(XYWH(element.bounds.right + 15, element.bounds.center_y, 8, 8), (255, 151, 135, 255))
        except ValueError:
            pass
