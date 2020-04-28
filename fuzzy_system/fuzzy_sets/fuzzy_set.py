from .point_2d import Point2D
import math


class FuzzySet(object):
    def __init__(self, smin : float, smax : float) -> None:
        self.points : [Point2D] = []
        self.min = smin
        self.max = smax

    def add_point(self, pt : Point2D) -> None:
        self.points.append(pt)
        self.points.sort()

    def add(self, x : float, y : float) -> None:
        self.add_point(Point2D(x, y))

    def __repr__(self) -> str:
        result = "[%.02f-%.02f]" % (self.min, self.max)
        result += "".join([str(pt) for pt in self.points])
        return result

    def __eq__(self, other) -> bool:
        return str(self) == str(other)

    def __ne__(self, other) -> bool:
        return str(self) != str(other)

    def __mul__(self, value : float):
        result = FuzzySet(self.min, self.max)
        for pt in self.points:
            result.add_point(Point2D(pt.x, pt.y * value))
        return result

    def __invert__(self):
        result = FuzzySet(self.min, self.max)
        for pt in self.points:
            result.add_point(Point2D(pt.x, 1 - pt.y))
        return result

    def value_out_of_bound(self, x_value : float) -> bool:
        return x_value < self.min or x_value > self.max

    def interpolated_value_between_two_points(self, x_value : float, 
                                        before : Point2D, after : Point2D):
        return (((before.y - after.y) * (after.x - x_value) 
                 / (after.x - before.x)) + after.y)

    def get_value_from_interpolation(self, x_value : float) -> float:
        points = [pt for pt in self.points if pt.x <= x_value]
        before = points[-1] if points else None
        points = [pt for pt in self.points if pt.x >= x_value]
        after = points[0] if points else None
        if before == after:
            return before.y
        else:
            return self.interpolated_value_between_two_points(x_value, 
                                                              before, after)

    def degree_at_value(self, x_value : float) -> float:
        if self.value_out_of_bound(x_value):
            return 0
        return self.get_value_from_interpolation(x_value)

    def sign(self, n : float) -> float:
        if n == 0:
            return 0
        return math.copysign(1, n)

    def merge(self, fs1, fs2, merge_func):
        result = FuzzySet(min(fs1.min, fs2.min), max(fs1.max, fs2.max))
        
        iter1, iter2 = iter(fs1.points), iter(fs2.points)
        end1, end2 = False, False
        pts1, pts2 = next(iter1), next(iter2)

        old_pt1 = pts1

        relative_position = 0
        new_relative_position = self.sign(pts1.y - pts2.y)

        while not end1 and not end2:

            x1 = pts1.x
            x2 = pts2.x
            relative_position = new_relative_position
            new_relative_position = self.sign(pts1.y - pts2.y)

            if relative_position != new_relative_position and relative_position != 0 and new_relative_position != 0:
                x = old_pt1.x if x1 == x2 else min(x1, x2)
                x_prime = max(x1, x2)
                slope1, slope2, delta = 0, 0, 0

                if x_prime != 0:
                    slope1 = (fs1.degree_at_value(x_prime) - fs1.degree_at_value(x)) / (x_prime - x)
                    slope2 = (fs2.degree_at_value(x_prime) - fs2.degree_at_value(x)) / (x_prime - x)

                if slope1 != slope2:
                    delta = (fs2.degree_at_value(x) - fs1.degree_at_value(x)) / (slope1 - slope2)

                result.add(x + delta, fs1.degree_at_value(x + delta))

                if x1 < x2:
                    old_pt1 = pts1
                    try:
                        pts1 = next(iter1)
                    except StopIteration:
                        end1 = True
                elif x1 > x2:
                    try:
                        pts2 = next(iter2)
                    except StopIteration:
                        end2 = True

            elif x1 == x2:
                result.add(x1, merge_func(pts1.y, pts2.y))
                old_pt1 = pts1
                try:
                    pts1 = next(iter1)
                except StopIteration:
                    end1 = True
                try:
                    pts2 = next(iter2)
                except StopIteration:
                    end2 = True
            elif x1 < x2:
                result.add(x1, merge_func(pts1.y, fs2.degree_at_value(x1)))
                old_pt1 = pts1
                try:
                    pts1 = next(iter1)
                except StopIteration:
                    end1 = True
            else:
                result.add(x2, merge_func(fs1.degree_at_value(x2), pts2.y))
                try:
                    pts2 = next(iter2)
                except StopIteration:
                    end2 = True

        if not end1:
            while not end1:
                result.add(pts1.x, merge_func(0, pts1.y))
                try:
                    pts1 = next(iter1)
                except StopIteration:
                    end1 = True
        elif not end2:
            while not end2:
                result.add(pts2.x, merge_func(0, pts2.y))
                try:
                    pts2 = next(iter2)
                except StopIteration:
                    end2 = True

        return result


    def __and__(self, other):
        return self.merge(self, other, min)

    def __or__(self, other):
        return self.merge(self, other, max)

    def centroid(self) -> float:
        if len(self.points) < 2:
            return 0
        ponderated_area, total_area = 0, 0
        local_area = None
        old_pt = None
        for new_pt in self.points:
            if not old_pt is None:
                local_area = min(old_pt.y, new_pt.y) * (new_pt.x - old_pt.x)
                factor = 1.0 / 2.0
                total_area += local_area
                ponderated_area += ((new_pt.x - old_pt.x) * factor + old_pt.x) * local_area
                if old_pt.y != new_pt.y:
                    local_area = (new_pt.x - old_pt.x) * (abs(new_pt.y - old_pt.y)) / 2
                    factor = 2.0 / 3.0 if new_pt.y > old_pt.y else 1.0 / 3.0
                    total_area += local_area
                    ponderated_area += ((new_pt.x - old_pt.x) * factor + old_pt.x) * local_area
                
            old_pt = new_pt
        centroid = ponderated_area / total_area
        return centroid


#if __name__ == '__main__':
#    fs = FuzzySet(10, 300)
#    fs.add_point(Point2D(100, 200))
#    fs.add(150, 210)
#    #print(fs)
#    #print(fs == fs)
#    #print(fs != fs)
#    #print(fs * 3)
#    #print(~fs)
#    #print(fs.value_out_of_bound(400))
#    #print(fs.value_out_of_bound(200))
#    #print(fs.get_value_from_interpolation(100))
#    #print(fs.degree_at_value(150))
#    #print(fs.degree_at_value(-20))
#    #print(fs.degree_at_value(400))
#    #print(fs.degree_at_value(100))
#    fs2 = FuzzySet(10, 300)
#    fs2.add_point(Point2D(100, 200))
#    fs2.add(150, 210)
#    #print(fs & fs2)
#    #print(fs | fs2)
#    print(fs.centroid())


    