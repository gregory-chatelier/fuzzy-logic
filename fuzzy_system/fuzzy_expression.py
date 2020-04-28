from .linguistic_variable import LinguisticVariable 

class FuzzyExpression(object):
    def __init__(self, lv : LinguisticVariable, value : str):
        self.lv = lv
        self.linguistic_value_name = value