import random

from operations import abstract_operation


class Minus(abstract_operation.AbstractOperation):
    a = 0
    b = 0

    def __init__(self):
        super().__init__("-", "Abziehen")

    def get_question(self):
        return "{} - {}".format(str(self.a), str(self.b))

    def solve(self):
        return int(self.a - self.b)

    def update(self):
        r1n = random.randint(0, 1000)
        r2n = random.randint(0, 1000)
        self.a = max(r1n, r2n)
        self.b = min(r1n, r2n)
