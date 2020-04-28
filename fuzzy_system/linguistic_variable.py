from .fuzzy_sets.fuzzy_set import FuzzySet
from .linguistic_value import LinguisticValue

class LinguisticVariable(object):
    def __init__(self, name : str, _min : float, _max : float) -> None:
        self.values : [LinguisticValue] = []
        self.name = name
        self.min = _min
        self.max = _max

    def add_value(self, lv : LinguisticValue):
        self.values.append(lv)

    def add_lv_value(self, name : str, fs : FuzzySet) -> None:
        self.add_value(LinguisticValue(name, fs))

    def clear_values(self):
        self.values = []

    def linguistic_value_by_name(self, name : str) -> LinguisticValue:
        name = name.upper()
        for value in self.values:
            if value.name.upper() == name:
                return value
        return None

#if __name__ == '__main__':
#    from fuzzy_sets.left_fuzzy_set import LeftFuzzySet
#    from fuzzy_sets.trapezoidal_fuzzy_set import TrapezoidalFuzzySet
#    from fuzzy_sets.right_fuzzy_set import RightFuzzySet

#    zoom = LinguisticVariable("Zoom", 1, 5)
#    zoom.add_value(LinguisticValue("Small", LeftFuzzySet(0, 5, 1, 2)))
#    zoom.add_value(LinguisticValue("Medium", TrapezoidalFuzzySet(0, 5, 1, 2, 3, 4)))
#    zoom.add_value(LinguisticValue("Large", RightFuzzySet(0, 5, 3, 4)))
#    print(zoom)
#    print(zoom.linguistic_value_by_name("medium"))
#    print(zoom.linguistic_value_by_name("medccc"))