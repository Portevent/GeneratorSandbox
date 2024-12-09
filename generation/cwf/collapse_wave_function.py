from abc import ABC
from typing import List

from generation import Generator
from generation.cwf.module.module import WCFModule


class WaveCollapseFunction(Generator, ABC):

    modules: List[WCFModule]