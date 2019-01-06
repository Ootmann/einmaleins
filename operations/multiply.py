import random

from operations import abstract_operation


class Multiply(abstract_operation.AbstractOperation):
    a = 0
    b = 0

    def __init__(self):
        super().__init__("x", "Multiplizieren")

    def get_question(self):
        return "{} x {}".format(str(self.a), str(self.b))

    def solve(self):
        return int(self.a * self.b)

    def update(self):
        self.a = random.randint(1, 10)
        self.b = random.randint(1, 10)
