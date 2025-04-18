from typing import Self

from color.image import Image


class ImagePalette:

    images: Image

    def __init__(self, images: List[Image] | None = None):
        self.images = images or []
        self.size = len(self.images)

    def add(self, image: Image) -> Self:
        self.images.append(image)
        self.size += 1
        return self

    def get(self, index: int) -> Image:
        if not (0 <= index < self.size):
            raise ImagePaletteException("Image index out of range")

        return self.image[index]

    