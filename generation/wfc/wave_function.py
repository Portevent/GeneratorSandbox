from typing import List, Dict

from canvas import Color
from generation.wfc.module import Module


class WaveFunction:

    _modules: List[Module]
    _colors: List[Color]
    modulesCount: int

    superpositionColorCache: Dict[bytes, Color]

    @property
    def modules(self) -> List[Module]:
        return self._modules

    @modules.setter
    def modules(self, modules: List[Module]):
        self._modules = modules
        self.modulesCount = len(modules)

    @property
    def colors(self) -> List[Color]:
        return self._colors

    @colors.setter
    def colors(self, colors: List[Color]):
        self._colors = colors

    def __init__(self, modules: List[Module], colors: List[Color]):
        self.modules = modules
        self.colors = colors
        self.superpositionColorCache = {}

    def getSuperpositionColor(self, modules: List[bool]):
        index = bytes(modules)
        return self.superpositionColorCache.get(index, self._addSuperpositionColor(modules))

    def _addSuperpositionColor(self, modules: List[bool]):
        r, g, b = 0, 0, 0
        i = 0
        for index, module in enumerate(modules):
            if module:
                _r, _g, _b = self.colors[self.modules[index].value].to_rgb()
                r += _r
                g += _g
                b += _b
                i += 1
        if i == 0:
            color = Color(0,0,0)
        else:
            if i > 1:
                i *= 2
            color = Color(r//i, g//i, b//i)
        self.superpositionColorCache[bytes(modules)] = color
        return color
