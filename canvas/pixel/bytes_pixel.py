from __future__ import annotations

from canvas.pixel import Pixel


class BytesPixel(Pixel):
    """
    BytesPixel are pixel that hold binary. Mainly useful for bit masking in WCF and such
    """
    value: bytes

    def __init__(self, value):
        self.value = value

    def set(self, element: bytes) -> None:
        self.value = element

    def get(self) -> bytes:
        return self.value

    def mask(self, other):
        self.value &= other

    @staticmethod
    def empty() -> BytesPixel:
        return BytesPixel(0)

    def __repr__(self) -> str:
        return f"<{self.value}>"

    def update(self, other: BytesPixel):
        self.value = other.get()
