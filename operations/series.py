import random

from operations import abstract_operation


class Series(abstract_operation.AbstractOperation):
    a = 0
    b = 0

    def __init__(self):
        super().__init__("series", "Zahlenreihen")

    def get_question(self):
        return "{} , {} , {} , {} , ?".format(self.a - 4 * self.b, self.a - 3 * self.b, self.a - 2 * self.b,
                                              self.a - 1 * self.b)

    def solve(self):
        return self.a

    def update(self):
        self.a = random.randint(100, 899)
        self.b = random.randint(1, 9) * random.choice([1, -1])
