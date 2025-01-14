from typing import TypedDict

from charm.game.generic import BaseEngine, AutoEngine, BaseDisplay

# -- ENGINES & DISPLAYS --
from charm.game.gamemodes.fnf import FNFEngine, FNFDisplay
from charm.game.gamemodes.four_key import FourKeyEngine, FourKeyDisplay
from charm.game.gamemodes.five_fret import FiveFretEngine, FiveFretDisplay
from charm.game.gamemodes.taiko import TaikoEngine, TaikoDisplay


# ?: Add other gamemode properties?
# !: We are doing a single engine per mode, prevents multiplayer, but lets leave that for after MVP
class GameModeDefinition(TypedDict):
    engines: type[BaseEngine]
    display: type[BaseDisplay]


GAMEMODES: dict[str, GameModeDefinition] = {
    'fnf': GameModeDefinition(engines=FNFEngine, display=FNFDisplay), # TODO: Doesn't work with Auto Engine
    '4k': GameModeDefinition(engines=FourKeyEngine, display=FourKeyDisplay),
    'hero': GameModeDefinition(engines=FiveFretEngine, display=FiveFretDisplay),
    'taiko': GameModeDefinition(engines=AutoEngine, display=TaikoDisplay)
}
