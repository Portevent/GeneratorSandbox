# Generator Sandbox

Generator Sandbox is a project template to iter over 2D tile generation.
It provide implementation of simple board that can be exported to png or gif files.

See [some examples](examples) on how to use the library, or see below

## Creating a board
`Board` are 2D array of cell which may contain `CellData`.

`CellData` can be any type. `GeneratorSandbox` provides `VisualData`, which is a `CellData` that can be visually represented.
`VisualData` can be as simple as a pixel, in that case `PixelData` can be used. It also can contains image, with `ImageData` which specifies its size and image.

There are two type of Board :
- `BaseBoard` that may contain any type of `CellData`
- `VisualBoard`, extending `BaseBoard`, which can be exported by painter to png or gif files. However, it requires cell to have `VisualData`.

```python
# Create an empty BaseBoard, where cells contain no data
board = BaseBoard.EMPTY(WIDTH, HEIGHT)

# Create an empty VisualBoard, where cells contain default PixelData (black pixel by drfault)
board = VisualBoard.EMPTY(WIDTH, HEIGHT, PixelData)

# Create a VisualBoard, that contains Image (cells are images rather than simple pixels).
# Each cell is created by the callback CreateImageData
# The last parameter (16, 16), specify the size of images within cells (must be coherent with what callback returns)
board = VisualBoard.FROM(WIDTH, HEIGHT, CreateImageData, (16,16))
```

Board map `Coordinate` to cells, with `Coordinate(0, 0)` being top left, and `Coordinate(width-1, height-1)` being bottom right.
```python
board = BaseBoard.EMPTY(10, 10)

cellA = board.get(Coordinate(0, 0)) # First cell
cellA.cell_data = ...

cellB = board.get(Coordinate(9, 9)) # Last cell
cellB.cell_data = ...

cellC = board.getRandomCoordinate()

for cell in board.getCellsInBox(Coordinate(4,5), Coordinate(9,9)):
    ...
```

## Generators
To automaticly edit cells and create procedural generation algorithm, you can use `Generator`.
This interface create the backbone of how an algorithm should be written.
We will later see `Manager`, that use this convention to automaticly run the algorithm, monitor its runtime and export the process to a png or gif file.

To help with the onboarding, some simple implementation of Generator are provided :

### Filler
Takes two Coordinate to iter over a board. You can provide a callback, so on each cell, it will use it

```python
def setRed(_: Coordinate, cell: BaseCell, __: float) -> None:
    cell.cell_data.setColor(Color.RED())

# This filler will set cells' PixelData's color to Red 
generator = Filler(start=Coordinate(2, 2), end=Coordinate(7,7)).do(setRed)
```

The callback takes three argument : the coordinate of the Cell, the cell itself, and the advancement (from 0 to 1) of the generator.
In the first example we only used the second argument cell, but the third one can be handy to make easy gradient :
```python
def setGradient(_: Coordinate, cell: BaseCell, advancement: float) -> None:
    cell.cell_data.setColor(Color.mix(Color.BLUE(), Color.GREEN(), advancement))

generator = Filler(start=Coordinate(2, 2), end=Coordinate(7,7)).do(setGradient)
```

## Manager 
TODO
