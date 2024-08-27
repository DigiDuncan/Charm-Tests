#
# -- CHARTSET AND CHART LOADING --
#
#   Before the unified menu can show the full list
#   charm needs to find all of the songs and charts.
#   To save time only the song metadata, and bare minimum
#   for each chart is found.
#
#   ! This is currently done per gamemode folder, but if a mod
#   ! in the future wants to mix gamemodes this will need updating.

# NOTE:
#   There are some major complications caused by FNF having two versions
#   which share file type. We also have to work around 4k and taiko both
#   using .osu files. This is solved in the mvp, but if we want chartsets
#   to mix gamemodes in the future we need to solve this issue.
#   FNF makes things harder again because there are also 'erect' versions
#   of some charts which currently means two chartsets from one folder.
#   This breaks a core assumption of Charm.

from typing import NamedTuple
from collections.abc import Callable
from pathlib import Path

from charm.lib.paths import songspath
from charm.lib.errors import ChartUnparseableError

from charm.refactor.generic.chartset import ChartSet
from charm.refactor.generic.chart import Chart, ChartMetadata

# -- PARSERS --
from charm.refactor.generic.parser import Parser
from charm.refactor.parsers.fnf import FNFParser
from charm.refactor.parsers.fnfv2 import FNFV2Parser
from charm.refactor.parsers.mania import ManiaParser
from charm.refactor.parsers.sm import SMParser
from charm.refactor.parsers.hero import HeroParser
from charm.refactor.parsers.taiko import TaikoParser

ParserChooser = Callable[[Path], bool]

class TypePair(NamedTuple):
    gamemode: str
    filetype: str

# TODO: Parse MIDI
gamemode_parsers: dict[str, tuple[type[Parser], ...]] = {
    'fnf': (FNFParser, FNFV2Parser),
    '4k': (ManiaParser, SMParser),
    'hero': (HeroParser,),
    'taiko': (TaikoParser,)
}


def load_gamemode_chartsets(gamemode: str) -> list[ChartSet]:
    parsers = gamemode_parsers[gamemode]
    all_gamemode_paths = (p for p in (songspath / gamemode).glob("**/*") if p.is_dir())
    chartsets = []
    for d in all_gamemode_paths:
        charts = []
        for parser in parsers:
            if not parser.is_possible_chartset(d):
                continue
            charts.extend(parser.parse_chart_metadata(d))
        if charts:
            chartset = ChartSet(d)
            chartset.charts = charts
            # TODO: Lyric events?
            chartsets.append(chartset)
    return chartsets


def load_chartsets() -> list[ChartSet]:
    gamemodes = ('fnf', '4k', 'hero', 'taiko')
    chartsets = []
    for gamemode in gamemodes:
        chartsets.extend(load_gamemode_chartsets(gamemode))
    return chartsets


def load_chart(chart_metadata: ChartMetadata) -> list[Chart]:
    parsers = gamemode_parsers[chart_metadata.gamemode]
    for parser in parsers:
        if parser.is_parsable_chart(chart_metadata.path):
            return parser.parse_chart(chart_metadata)
    raise ChartUnparseableError(message=f'chart: {chart_metadata} cannot be parsed by any parser for gamemode {chart_metadata.gamemode}')
