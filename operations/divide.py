import random

from operations import abstract_operation


class Divide(abstract_operation.AbstractOperation):
    a = 0
    b = 0

    def __init__(self):
        super().__init__(":", "Teilen")

    def get_question(self):
        return "{} : {}".format(str(self.a), str(self.b))

    def solve(self):
        return int(self.a / self.b)

    def update(self):
        r1n = random.randint(1, 10)
        r2n = random.randint(1, 10)
        self.a = r1n * r2n
        self.b = r2n
