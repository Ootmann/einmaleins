import random

from operations import abstract_operation


class Round(abstract_operation.AbstractOperation):
    a = 0
    b = 0

    def __init__(self):
        super().__init__("round", "Runden")

    def get_question(self):
        if self.b == -1:
            return "{} auf den nächsten Zehner runden".format(self.a)
        elif self.b == -2:
            return "{} auf den nächsten Hunderter runden".format(self.a)

    def solve(self):
        return int(round(self.a, self.b))

    def update(self):
        self.a = random.randint(0, 999)
        self.b = random.randint(1, 2) * -1
