class CartesianPixel(Pixel, ABC):

    # Specify how many dimensions this class works with
    dimensions: int | None = None

    @abstracmethod
    @staticmethod
    def generate(cls, dimensionsMin: Tuple, dimensionsMax: Tuple, empty: Callable[[], CartesianPixel] | None = None) -> Dict[Tuple, CartesianPixel]:
        """
        Generate a dictionary of pixels
        """
        raise NotImplementedError()