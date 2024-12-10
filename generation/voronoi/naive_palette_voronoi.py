from generation.voronoi.naive_linked_voronoi import NaiveLinkedVoronoi
from generation.voronoi.naive_list_voronoi import NaiveListVoronoi
from generation.voronoi.naive_set_voronoi import NaiveSetVoronoi
from generation.voronoi.palette_voronoi import PaletteVoronoi


class NaivePaletteVoronoi(PaletteVoronoi, NaiveLinkedVoronoi):
    pass