from .fuzzy_expression import FuzzyExpression
from .fuzzy_sets.fuzzy_set import FuzzySet
from .fuzzy_value import FuzzyValue
from .linguistic_value import LinguisticValue

class FuzzyRule(object):

    def __init__(self, rule_str : str, fs) -> None:
        rule_str = rule_str.upper()
        premises = []
        conclusion = None

        rule = rule_str.split(" THEN ")
        if len(rule) == 2:
            rule[0] = rule[0][2:]
            prem = rule[0].strip().split(" AND ")
            for exp in prem:
                res = exp.split(" IS ")
                if len(res) == 2:
                    premises.append(FuzzyExpression(fs.linguistic_variable_by_name(res[0]), res[1]))
            conclu = rule[1].split(" IS ")
            if len(conclu) == 2:
                conclusion = FuzzyExpression(fs.linguistic_variable_by_name(conclu[0]), conclu[1])

        self.premises = premises
        self.conclusion = conclusion

        self.val : LinguisticValue =  None
        self.rule_premise : FuzzyExpression = None
        self.problem_value : FuzzyValue = None
        self.rule_degree : float = None

    def compute_degree(self) -> float:
        self.val = self.rule_premise.lv.linguistic_value_by_name(self.rule_premise.linguistic_value_name)
        if self.val is None:
            return None
        return self.val.degree_at_value(self.problem_value.value)

    def get_degree(self, problem : [FuzzyValue]) -> float:
        self.val = None
        for problem_value in problem:
            self.problem_value = problem_value
            if self.rule_premise.lv == self.problem_value.lv:
                return self.compute_degree()
        return 0

    def apply(self, problem : [FuzzyValue]) -> FuzzySet:
        self.rule_degree = 1
        for premise in self.premises:
            self.rule_premise = premise
            degree = self.get_degree(problem)
            if self.val is None:
                return None 
            self.rule_degree = min(self.rule_degree, degree)
        return self.conclusion.lv.linguistic_value_by_name(self.conclusion.linguistic_value_name).fs * self.rule_degree
