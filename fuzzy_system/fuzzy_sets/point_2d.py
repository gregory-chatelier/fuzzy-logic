class Point2D(object):
    def __init__(self, x : float, y : float) -> None:
        self.x = x
        self.y = y

    def __eq__(self, other) -> bool:
        return self.x == other.x

    def __ne__(self, other) -> bool:
        return self.x != other.x

    def __lt__(self, other) -> bool:
        return self.x < other.x

    def __le__(self, other) -> bool:
        return self.x <= other.x

    def __gt__(self, other) -> bool:
        return self.x > other.x

    def __ge__(self, other) -> bool:
        return self.x >= other.x

    def __repr__(self) -> str:
        return "(%.02f;%.02f)" % (self.x, self.y)

#if __name__ == '__main__':
#    pt1 = Point2D(100, 200)
#    pt2 = Point2D(150, 200)
#    print(f"{pt1} > {pt2} ? {pt1 > pt2}")
#    print(f"{pt1} < {pt2} ? {pt1 < pt2}")
#    print(f"{pt1} >= {pt2} ? {pt1 >= pt2}")
#    print(f"{pt1} >= {pt1} ? {pt1 >= pt1}")
#    print(f"{pt1} <= {pt2} ? {pt1 <= pt2}")
#    print(f"{pt1} <= {pt1} ? {pt1 <= pt1}")
#    print(f"{pt1} == {pt1} ? {pt1 == pt1}")
#    print(f"{pt1} != {pt1} ? {pt1 != pt1}")