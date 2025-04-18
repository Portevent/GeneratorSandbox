from typing import Self

from color.image import Image


class ImagePalette:

    images: Image

    def __init__(self):
        self.images = []
        self.size = 0

    def add(self, image: Image) -> Self:
        self.images.append(image)
        self.size += 1
        return self

    def get(self, index: int) -> Image:
        pass