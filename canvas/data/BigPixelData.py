from canvas.data.PixelData import PixelData


class BigPixelData(PixelData):
    """
    Big Pixel
    """


    @property
    def width(self) -> int:
        return 10

    @property
    def height(self) -> int:
        return 10
