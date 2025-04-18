from typing import Self

from color.image import Image


class ImagePaletteHelper:

    @staticmethod
    def FromFiles(files: List[str]) -> ImagePalette:
        return palette([ImageLoader.from_file(file) for file in files])

    @staticmethod
    def FromDir(dir: str) -> ImagePalette:
        return ImagePaletteHelper.FromFiles([file for file in Path(dir).iterdir() if file.is_file()])
