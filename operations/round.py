import random

from operations import abstract_operation
from decimal import *


class Round(abstract_operation.AbstractOperation):
    a = 0
    b = 0

    def __init__(self):
        super().__init__("round", "Runden")

    def get_question(self):
        if self.b == 10:
            return "{} auf den nächsten Zehner runden".format(self.a)
        elif self.b == 100:
            return "{} auf den nächsten Hunderter runden".format(self.a)

    def solve(self):
        return (self.a / Decimal(str(self.b))).quantize(0, ROUND_HALF_UP) * self.b

    def update(self):
        self.a = Decimal(str(random.randint(0, 999)))
        self.b = random.choice(10, 100)
