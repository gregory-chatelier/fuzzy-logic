from .fuzzy_set import FuzzySet
from .point_2d import Point2D

class TriangularFuzzySet(FuzzySet):
    def __init__(self, _min : float, _max : float, 
                 triangle_begin : float, triangle_center : float, triangle_end : float):
        super().__init__(_min, _max)
        self.add_point(Point2D(_min, 0))
        self.add_point(Point2D(triangle_begin, 0))
        self.add_point(Point2D(triangle_center, 1))
        self.add_point(Point2D(triangle_end, 0))
        self.add_point(Point2D(_max, 0))

if __name__ == '__main__':
    fs = TriangularFuzzySet(0, 5, 1, 2, 3)
    print(fs)