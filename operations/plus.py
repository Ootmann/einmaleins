from operations import abstract_operation


class Plus(abstract_operation.AbstractOperation):

    def __init__(self):
        super().__init__("+", "Addieren")

    def get_question(self, a, b):
        return "{} + {}".format(str(a), str(b))

    def solve(self, a, b):
        return int(a + b)
