from SOLID_Solution.Rules.premium_allowance_rule import premium_allowance_rule
from SOLID_Solution.Rules.standard_allowance_rule import standard_allowance_rule
from SOLID_Solution.package_type import package_type


class book_allowance_setter:
    def __init__(self, student):
        self.student = student
        self.rules[package_type.Premium] = premium_allowance_rule()
        self.rules[package_type.Standard] = standard_allowance_rule()

    def set_allowance(self, the_package_type):
        factor = self.rules[the_package_type].get_factor()
        self.student
