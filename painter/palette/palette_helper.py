import random

from color import Color
from painter.palette import Palette


class PaletteHelper:
    """
    Helper class to create palette objects
    Each method takes parameters, but also an optional palette.
    If this one is specified, no new palette will be created and instead colors will be added to the existing palette.
    """

    @staticmethod
    def random(colors: int, palette: Palette | None = None) -> Palette:
        """
        Create a palette of *colors* random color
        Note : color may be dark, see randomHue for bright full colors
        :param colors: size of the palette
        :param palette: if specified, add colors to the palette instead
        """
        if palette is None:
            palette = Palette()

        for i in range(colors):
            palette.save(Color.from_hsv(int(random.random()*360), random.random(), random.random()))

        return palette

    @staticmethod
    def randomHue(hues: int, palette: Palette | None = None) -> Palette:
        """
        Create a palette of *hues* random hues
        :param hues: size of the palette
        :param palette: if specified, add colors to the palette instead
        """
        if palette is None:
            palette = Palette()

        for i in range(hues):
            palette.save(Color.from_hsv(int(random.random()*360), 1, 1))

        return palette

    @staticmethod
    def distinctHue(hues: int, palette: Palette | None = None) -> Palette:
        """
        Create a palette of *hues* distinct hues
        :param hues: size of the palette
        :param palette: if specified, add colors to the palette instead
        """
        if palette is None:
            palette = Palette()

        for hue in range(0, 360, int(360 / hues)):
            palette.save(Color.from_hsv(hue, 1, 1))

        return palette

    @staticmethod
    def rangeHue(hue: int, variants: int, min_value: float = 0, palette: Palette | None = None) -> Palette:
        """
        Create an HSV palette of *hue*, with *variants* variations of value (going to 1 to *min_value*)
        :param hue: hue of the palette
        :param variants: number of variants
        :param min_value: minimum value of the darkest color (value as in HSV)
        :param palette: if specified, add colors to the palette instead
        """
        if palette is None:
            palette = Palette()
        step = (1-min_value)/variants
        value = 1
        for i in range(variants):
            palette.save(Color.from_hsv(hue, 1, value))
            value -= step

        return palette

    @staticmethod
    def randomRangeHue(variants: int, min_value: float = 0, palette: Palette | None = None) -> Palette:
        """
        Create an HSV palette of a random hue, with *variants* variations of value (going to 1 to *min_value*)
        :param variants: number of variants
        :param min_value: minimum value of the darkest color (value as in HSV)
        :param palette: if specified, add colors to the palette instead
        """
        if palette is None:
            palette = Palette()
        return PaletteHelper.rangeHue(int(random.random()*360), variants, min_value, palette)


    @staticmethod
    def randomRangeHues(hues: int, variants: int, min_value: float = 0, palette: Palette | None = None) -> Palette:
        """
        Create an HSV palette of *hues* random hues, each with *variants* variations of value
        :param hues: number of different hues
        :param variants: number of different variations for each hue
        :param min_value: minimum value of the darkest color (value as in HSV)
        :param palette: if specified, add colors to the palette instead
        """
        if palette is None:
            palette = Palette()

        for i in range(hues):
            hue = int(random.random()*360)
            PaletteHelper.rangeHue(hue, variants, min_value=min_value, palette=palette)

        return palette


    @staticmethod
    def distinctRangeHues(hues: int, variants: int, min_value: float = 0, palette: Palette | None = None) -> Palette:
        """
        Create an HSV palette of *hues* distinct hues, each with *variants* variations of value
        :param hues: number of different hues
        :param variants: number of different variations for each hue
        :param min_value: minimum value of the darkest color (value as in HSV)
        :param palette: if specified, add colors to the palette instead
        """
        if palette is None:
            palette = Palette()

        for hue in range(0, 360, int(360 / hues)):
            PaletteHelper.rangeHue(hue, variants, min_value=min_value, palette=palette)

        return palette
