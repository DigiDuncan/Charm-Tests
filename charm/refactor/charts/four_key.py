from __future__ import annotations

import logging
from typing import Any, Literal
from charm.lib.types import Range4, Seconds
from charm.refactor.generic.chart import Chart, Note

logger = logging.getLogger("charm")

class FourKeyNoteType:
    NORMAL = "normal"
    BOMB = "bomb"
    DEATH = "death"
    HEAL = "heal"
    CAUTION = "caution"
    STRIKELINE = "strikeline"

class FourKeyNote(Note):
    def __init__(self, chart: Chart, time: Seconds, lane: Range4,
                 length: Seconds = 0, type: str = "normal",
                 hit: bool = False, missed: bool = False,
                 hit_time: Seconds | None = None,
                 extra_data: tuple[Any, ...] | None = None,
                 parent: FourKeyNote | None = None):
        super().__init__(chart, time, lane, length, type, hit, missed, hit_time, extra_data)
        self.parent = parent
        self.lane: Range4

    def __lt__(self, other: FourKeyNote):
        return (self.time, self.lane, self.type) < (other.time, other.lane, other.type)

class FourKeyChart(Chart):
    def __init__(self, difficulty: str, hash: str | None):
        super().__init__("4k", difficulty, "4k", 4, hash)
