# stdlib
import pathlib
from .main import *


def get_version() -> str:
    with open(str(pathlib.Path(__file__).parent / 'version.txt'), mode='r') as version_file:
        version = version_file.readline().strip()
    return version


__title__ = pathlib.Path(__file__).parts[-2]
__version__ = get_version()
__name__ = __title__
