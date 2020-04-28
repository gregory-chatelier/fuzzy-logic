from .fuzzy_set import FuzzySet
from .point_2d import Point2D

class TrapezoidalFuzzySet(FuzzySet):
    def __init__(self, _min : float, _max : float, 
                 base_left : float, height_left : float,
                 height_right : float, base_right : float):
        super().__init__(_min, _max)
        self.add_point(Point2D(_min, 0))
        self.add_point(Point2D(base_left, 0))
        self.add_point(Point2D(height_left, 1))
        self.add_point(Point2D(height_right, 1))
        self.add_point(Point2D(base_right, 0))
        self.add_point(Point2D(_max, 0))

if __name__ == '__main__':
    fs = TrapezoidalFuzzySet(0, 5, 1, 2, 3, 4)
    print(fs)