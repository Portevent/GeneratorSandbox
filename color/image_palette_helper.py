from typing import Self

from color.image import Image


class ImagePaletteHelper:

    @staticmethod
    def FromFiles(files: List[str]) -> ImagePalette:
        return palette([ImageLoader.from_file(file) for file in files])
