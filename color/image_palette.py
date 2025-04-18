from typing import Self, List, Tuple

from color.image import Image


class ImagePaletteException(Exception):
    pass


class ImagePalette:

    images: List[Image]

    width: int
    height: int

    def __init__(self, images: List[Image] | None = None):
        self.images = images or []
        self.size = len(self.images)

    def __init__(self, images: List[Tuple[Image, int, int]]):
        self.images = [image[0] for image in images]
        self.size = len(self.images)
        self.setVisualSize(images[0][1], images[0][2])

    def setVisualSize(self, width: int, height: int):
        self.width = width
        self.height = height

    def add(self, image: Image) -> Self:
        self.images.append(image)
        self.size += 1
        return self

    def get(self, index: int) -> Image:
        if not (0 <= index < self.size):
            raise ImagePaletteException("Image index out of range")

        return self.images[index]

    