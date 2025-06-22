"""

from pkg_resources import resource_filename

DATA_ROOT = resource_filename('langcodes', 'data')
import os


def data_filename(filename):
    return os.path.join(DATA_ROOT, filename)

"""
from pathlib import Path
from typing import Final

import xbmcaddon
import xbmc

ADDON: xbmcaddon = None
try:
    ADDON = xbmcaddon.Addon()
except Exception:
    xbmc.log('xbmcaddon.Addon was not found.', level=xbmc.LOGERROR)

ADDON_PATH: Final[Path] = Path(ADDON.getAddonInfo('path'))
RESOURCES_PATH: Final[Path] = ADDON_PATH.joinpath('resources')
TOP_PACKAGE_PATH: Final[Path] = RESOURCES_PATH.joinpath('lib')
LANG_CODES_PATH: Final[Path] = TOP_PACKAGE_PATH / 'langcodes' / 'data'


def data_filename(filename: str) -> str:
    result: str = str(LANG_CODES_PATH / filename)
    xbmc.log(f'langcodes_filename: {result}')
    return result
