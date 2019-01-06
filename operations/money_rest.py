import decimal
import random

from operations import abstract_operation


class MoneyRest(abstract_operation.AbstractOperation):
    euro_notes = (5, 10, 20, 50, 100, 200, 500)
    a = 0
    b = 0

    def __init__(self):
        super().__init__("money_rest", "Restgeld berechnen")

    def get_question(self):
        return "Du bezahlst {} € mit einem {} € Schein. Rückgeld?".format(str(self.a).replace('.', ','), self.b)

    def solve(self):
        return '{0:.2f}'.format(self.b - self.a).replace('.', ',') + " €"

    def update(self):
        r1n = decimal.Decimal(
            str(random.randint(1, 499)) + "." + str(random.randint(0, 9)) + str(random.randint(0, 9)))
        r2n = 0
        for note in self.euro_notes:
            if note > r1n:
                r2n = note
                break
        if r2n < r1n:
            raise Exception("No matching note found")
        self.a = r1n
        self.b = r2n
