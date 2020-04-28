from .fuzzy_set import FuzzySet
from .point_2d import Point2D

class RightFuzzySet(FuzzySet):
    def __init__(self, _min : float, _max : float, 
                 height_min : float, base_max : float):
        super().__init__(_min, _max)
        self.add_point(Point2D(_min, 0))
        self.add_point(Point2D(height_min, 0))
        self.add_point(Point2D(base_max, 1))
        self.add_point(Point2D(_max, 1))

if __name__ == '__main__':
    fs = RightFuzzySet(0, 5, 3, 4)
    print(fs)