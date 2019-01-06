import decimal
import random

from operations import abstract_operation


class MoneyAdd(abstract_operation.AbstractOperation):
    a = 0
    b = 0

    def __init__(self):
        super().__init__("money_add", "Geld zusammenzählen")

    def get_question(self):
        return "{} € + {} €".format(self.a, self.b).replace('.', ',')

    def solve(self):
        return '{0:.2f}'.format(self.a + self.b).replace('.', ',') + " €"

    def update(self):
        self.a = decimal.Decimal(
            str(random.randint(1, 499)) + "." + str(random.randint(0, 9)) + str(random.randint(0, 9)))
        self.b = decimal.Decimal(
            str(random.randint(1, 499)) + "." + str(random.randint(0, 9)) + str(random.randint(0, 9)))
