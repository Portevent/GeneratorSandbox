from pathlib import Path
from typing import List

from color.image import ImageLoader
from color.image_palette import ImagePalette


class ImagePaletteHelper:

    @staticmethod
    def FromFiles(files: List[str]) -> ImagePalette:
        return ImagePalette([ImageLoader.from_file(file) for file in files])

    @staticmethod
    def FromDir(directory: str) -> ImagePalette:
        return ImagePaletteHelper.FromFiles([file for file in Path(directory).iterdir() if file.is_file()])
