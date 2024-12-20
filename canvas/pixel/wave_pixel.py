from __future__ import annotations

import random
from typing import List, Set, Self, Tuple

from canvas import Color
from canvas.pixel.linked_ortho_2d_pixel import LinkedOrtho2DPixel
from canvas.pixel.linked_surrond_2d_pixel import LinkedSurround2DPixel
from canvas.pixel.pixel import Point
from generation.wfc.wave_function import WaveFunction


def _isAvailable(keyValue: Tuple) -> bool:
    return keyValue[1]

class WavePixel[T: List[bool]](LinkedSurround2DPixel):

    possibleValues: Set[int]

    collapsed: bool

    waveFunction: WaveFunction

    color: Color

    entropy: float

    def __init__(self, element: T | None = None, point: Point | None = None, waveFunction: WaveFunction | None = None) -> None:
        super().__init__(element, point)
        self.waveFunction = waveFunction
        self.possibleValues = set(range(len(self.waveFunction.colors)))
        self.element = [True] * self.waveFunction.modulesCount
        self.color = self.waveFunction.getSuperpositionColor(self.element)
        self.entropy = waveFunction.modulesCount
        self.collapsed = False

    def checkRules(self):
        if self.entropy <= 1:
            return

        changed = False
        neighbor = self.neighbors
        for index, module in enumerate(self.element):
            if not module:
                continue

            rule = self.waveFunction.modules[index].neighbors
            own = self.waveFunction.modules[index].value
            if not self._checkRule(neighbor, rule, ownValue=own):
                changed = True
                self.element[index] = False

        if changed:
            self.updateWave()


    def _checkRule(self, neighbors: List[Self | None], values: List[T], ownValue: T):
        for i in range(self.neighborsSize):
            if neighbors[i] is None:
                continue

            # if values[i] not in neighbors[i].possibleValues:
            if (values[i] if values[i] >= 0 else ownValue) not in neighbors[i].possibleValues:
                return False


        return True

    def _getPossibleModules(self) -> List[int]:
        return [index for index, _ in filter(_isAvailable, enumerate(self.element))]

    def _getPossibleValues(self, modules: List[int] | None = None) -> Set[int]:
        return set([self.waveFunction.modules[index].value for index in (modules or self._getPossibleModules())])

    def collapse(self, finalModule: int | None = None):
        if self.collapsed:
            return False

        self.collapsed = True

        if finalModule is None:
            try:
                self.checkRules()
                finalModule = random.choice(self._getPossibleModules())
            except IndexError: # Impossible case
                self.element = [True] * self.waveFunction.modulesCount
                self.updateWave()
                return False


        self.element = [False] * self.waveFunction.modulesCount
        self.element[finalModule] = True
        self.updateWave()
        return True


    def updateWave(self):
        newValues = self._getPossibleValues()
        change = len(newValues) < len(self.possibleValues)
        self.possibleValues = set(newValues)
        self.color = self.waveFunction.getSuperpositionColor(self.element)
        self.entropy = len(self.possibleValues)
        self.entropy = sum(self.element)
        if change and self.entropy > 0:
            for neighbor in self.neighbors:
                if neighbor:
                    neighbor.checkRules()

    def getColor(self) -> Tuple[int, int, int]:
        return self.color.to_rgb()

    def __repr__(self) -> str:
        return f"[{self.point}: {self.possibleValues}]"

    def __eq__(self, other):
        return self.point == other.point

    def __hash__(self):
        return hash(self.point)