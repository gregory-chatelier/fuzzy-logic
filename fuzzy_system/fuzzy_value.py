from .linguistic_variable import LinguisticVariable 

class FuzzyValue(object):
    def __init__(self, lv : LinguisticVariable, value : float):
        self.lv = lv
        self.value = value
