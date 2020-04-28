from .fuzzy_sets.fuzzy_set import FuzzySet

class LinguisticValue(object):
    def __init__(self, name : str, fs : FuzzySet) -> None:
        self.name = name
        self.fs = fs

    def degree_at_value(self, value : float) -> float:
        return self.fs.degree_at_value(value)
