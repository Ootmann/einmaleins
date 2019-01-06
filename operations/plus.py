import random

from operations import abstract_operation


class Plus(abstract_operation.AbstractOperation):
    a = 0
    b = 0

    def __init__(self):
        super().__init__("+", "Addieren")

    def get_question(self):
        return "{} + {}".format(str(self.a), str(self.b))

    def solve(self):
        return int(self.a + self.b)

    def update(self):
        r1n = random.randint(0, 1000)
        r2n = random.randint(0, 1000)
        r12 = [max(r1n, r2n) - min(r1n, r2n), min(r1n, r2n)]
        random.shuffle(r12)
        self.a = r12[0]
        self.b = r12[1]
