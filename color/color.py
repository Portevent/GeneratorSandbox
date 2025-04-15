from __future__ import annotations

from typing import Self


class Color:
    """
    Color helper class
    """

    _r: int
    _g: int
    _b: int

    @property
    def r(self) -> int:
        return self._r

    @property
    def g(self) -> int:
        return self._g

    @property
    def b(self) -> int:
        return self._b

    @r.setter
    def r(self, r: int) -> None:
        self._r = min(256, max(r, 0))

    @g.setter
    def g(self, g: int) -> None:
        self._g = min(256, max(g, 0))

    @b.setter
    def b(self, b: int) -> None:
        self._b = min(256, max(b, 0))

    def __init__(self, r: int = 0, g: int = 0, b: int = 0):
        """
        Create a new Color
        :param r: Red
        :param g: Green
        :param b: Blue
        """
        self.r = r
        self.g = g
        self.b = b

    def to_hex(self) -> str:
        """
        Convert to hex (#ff0000)
        :return: hex string
        """
        return "#" + format(self._r, '02x') + format(self._g, '02x') + format(self._b, '02x')

    def to_int(self) -> int:
        """
        Convert to int from 0 to 16777215
        :return: int number
        """
        return self._r * 256 * 256 + self._g * 256 + self._b

    def to_rgb(self) -> tuple[int, int, int]:
        """
        Convert to tuple (r, g, b)
        :return: tuple (r, g, b)
        """
        return self._r, self._g, self._b

    def add(self, amount: int) -> Self:
        """
        Add amount to each R, G and B components
        :param amount: amount to add
        :return: self
        """
        self.r += amount
        self.g += amount
        self.b += amount
        return self

    def __str__(self):
        return str(self.to_hex())

    def __repr__(self):
        return f"[{self._r}/{self._g}/{self._b}]"

    def __hash__(self):
        return self.to_int()

    @staticmethod
    def from_hex(hex_str: str) -> Color:
        """
        Create a new Color from hex string e.g. ff0000 (without the #)
        :param hex_str: hex string
        :return: Color
        """
        return Color(int(hex_str[0:2], 16), int(hex_str[2:4], 16), int(hex_str[4:6], 16))

    @staticmethod
    def from_rgb(r: int, g: int, b: int) -> Color:
        """
        Create a new Color from RGB components
        :param r: red
        :param g: green
        :param b: blue
        :return: Color
        """
        return Color(r, g, b)

    @staticmethod
    def from_1rgb(r: float, g: float, b: float) -> Color:
        """
        Create a Color from R,G,B values between 0 and 1
        (For 0 to 255, see "from_rgb")
        :param r: Red
        :param g: Green
        :param b: Blue
        :return: Color
        """
        return Color(int(r * 255), int(g * 255), int(b * 255))

    @staticmethod
    def from_int(rgb: int) -> Color:
        """
        Create a Color from integer value (0 to 16777215)
        :param rgb: integer value
        :return: Color
        """
        return Color(rgb // 65536, rgb // 256 % 256, rgb % 256)

    @staticmethod
    def from_hsv(hue: int, saturation: float, value: float) -> Color:
        """
        Create a Color from HSV components
        :param hue: 0 to 360
        :param saturation: 0 to 1
        :param value: 0 to 1
        :return: Color
        """
        chroma = value * saturation
        h_prime = (hue % 360) / 60
        x = chroma * (1 - abs(h_prime % 2 - 1))
        r: float
        g: float
        b: float

        if h_prime < 1:
            r, g, b = chroma, x, 0
        elif h_prime < 2:
            r, g, b = x, chroma, 0
        elif h_prime < 3:
            r, g, b = 0, chroma, x
        elif h_prime < 4:
            r, g, b = 0, x, chroma
        elif h_prime < 5:
            r, g, b = x, 0, chroma
        else:
            r, g, b = chroma, 0, x

        m = value - chroma
        r += m
        g += m
        b += m
        return Color.from_1rgb(r, g, b)

    @classmethod
    def BLACK(cls):
        return cls.from_rgb(0, 0, 0)

    @classmethod
    def RED(cls):
        return cls.from_rgb(255, 0, 0)

    @classmethod
    def GREEN(cls):
        return cls.from_rgb(0, 255, 0)

    @classmethod
    def BLUE(cls):
        return cls.from_rgb(0, 0, 255)

    @classmethod
    def WHITE(cls):
        return cls.from_rgb(255, 255, 255)

    @staticmethod
    def mix(colorA: Color, colorB: Color, mix: float = 0.5) -> Color:
        return Color.from_rgb(int(colorA.r * (1-mix) + colorB.r * mix),
                              int(colorA.g * (1-mix) + colorB.g * mix),
                              int(colorA.b * (1-mix) + colorB.b * mix))

