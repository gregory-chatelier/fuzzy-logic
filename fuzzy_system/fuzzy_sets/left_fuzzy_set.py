from .fuzzy_set import FuzzySet
from .point_2d import Point2D

class LeftFuzzySet(FuzzySet):
    def __init__(self, _min : float, _max : float, 
                 height_max : float, base_min : float):
        super().__init__(_min, _max)
        self.add_point(Point2D(_min, 1))
        self.add_point(Point2D(height_max, 1))
        self.add_point(Point2D(base_min, 0))
        self.add_point(Point2D(_max, 0))

if __name__ == '__main__':
    fs = LeftFuzzySet(0, 5, 1, 2)
    print(fs)
