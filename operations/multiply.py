from operations import abstract_operation


class Multiply(abstract_operation.AbstractOperation):

    def __init__(self):
        super().__init__("x", "Multiplizieren")

    def get_question(self, a, b):
        return "{} x {}".format(str(a), str(b))

    def solve(self, a, b):
        return int(a * b)
