from .linguistic_variable import LinguisticVariable
from .fuzzy_rule import FuzzyRule
from .fuzzy_value import FuzzyValue
from .fuzzy_sets.fuzzy_set import FuzzySet

class FuzzySystem(object):
    def __init__(self, name : str) -> None:
        self.name = name
        self.inputs : [LinguisticVariable] = []
        self.rules : [FuzzyRule] = []
        self.problem : [FuzzyValue] = []
        self.output : LinguisticVariable = None

    def add_input_variable(self, lv : LinguisticVariable) -> None:
        self.inputs.append(lv)

    def add_output_variable(self, lv : LinguisticVariable) -> None:
        self.output = lv

    def add_fuzzy_rule_by_rule(self, rule : FuzzyRule) -> None:
        self.rules.append(rule)

    def add_fuzzy_rule(self, rule : str) -> None:
        self.add_fuzzy_rule_by_rule(FuzzyRule(rule, self))

    def set_input_variable(self, _input : LinguisticVariable, value : float) -> None:
        self.problem.append(FuzzyValue(_input, value))

    def reset_case(self) -> None:
        self.problem.clear()

    def linguistic_variable_by_name(self, name : str) -> LinguisticVariable:
        name = name.upper()
        for _input in self.inputs:
            if _input.name.upper() == name:
                return _input
        if self.output.name.upper() == name:
            return self.output
        return None

    def solve(self) -> float:
        res = FuzzySet(self.output.min, self.output.max)
        res.add(self.output.min, 0)
        res.add(self.output.max, 0)
        for rule in self.rules:
            resulting_set = rule.apply(self.problem)
            if not resulting_set is None:
                res = res | resulting_set
        return res.centroid()