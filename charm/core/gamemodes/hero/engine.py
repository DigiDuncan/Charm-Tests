from typing import NamedTuple

from charm.core.generic.engine import DigitalKeyEvent
from charm.lib.keymap import keymap
from charm.lib.types import Seconds

from charm.core.generic import Engine, EngineEvent, Judgement
from .chart import HeroChart, HeroNote

class ChordShape(NamedTuple):
    green: bool
    red: bool
    yellow: bool
    blue: bool
    orange: bool

    def __repr__(self) -> str:
        return f"<ChordShape {'G' if self.green else '_'}{'R' if self.red else '_'}{'Y' if self.yellow else '_'}{'B' if self.blue else '_'}{'O' if self.orange else '_'}>"

class ChordShapeChangeEvent(EngineEvent):
    def __init__(self, time: Seconds, chord_shape: ChordShape):
        super().__init__(time)
        self.chord_shape = chord_shape

class HeroEngine(Engine[HeroChart, HeroNote]):
    def __init__(self, chart: HeroChart, offset: Seconds = 0):
        # Defaulting to 80ms hit window, despite CH's ~140ms, because that's egregiously large.
        judgements = [
            Judgement('Pass', 'pass', 80, 10, 1),
            Judgement('Miss', 'miss', float('inf'), 0, 0),
        ]
        super().__init__(chart, judgements, offset)

        self.current_events: list[ChordShapeChangeEvent | DigitalKeyEvent] = []

    def on_key_press(self, symbol: int, modifiers: int) -> None:
        if symbol in (keymap.hero.green, keymap.hero.red, keymap.hero.yellow, keymap.hero.blue, keymap.hero.orange):
            self.current_events.append(ChordShapeChangeEvent(self.chart_time, ChordShape(
                keymap.hero.green.held,
                keymap.hero.red.held,
                keymap.hero.yellow.held,
                keymap.hero.blue.held,
                keymap.hero.orange.held
            )))

        elif symbol == keymap.hero.strumup:
            self.current_events.append(DigitalKeyEvent(self.chart_time, "strumup", "down"))
        elif symbol == keymap.hero.strumdown:
            self.current_events.append(DigitalKeyEvent(self.chart_time, "strumdown", "down"))

    def on_key_release(self, symbol: int, modifiers: int) -> None:
        if symbol in (keymap.hero.green, keymap.hero.red, keymap.hero.yellow, keymap.hero.blue, keymap.hero.orange):
            self.current_events.append(ChordShapeChangeEvent(self.chart_time, ChordShape(
                keymap.hero.green.held,
                keymap.hero.red.held,
                keymap.hero.yellow.held,
                keymap.hero.blue.held,
                keymap.hero.orange.held
            )))

        elif symbol == keymap.hero.strumup:
            self.current_events.append(DigitalKeyEvent(self.chart_time, "strumup", "up"))
        elif symbol == keymap.hero.strumdown:
            self.current_events.append(DigitalKeyEvent(self.chart_time, "strumdown", "up"))