from operations import abstract_operation


class Series(abstract_operation.AbstractOperation):

    def __init__(self):
        super().__init__("series", "Zahlenreihen")

    def get_question(self, a, b):
        return "{} , {} , {} , {} , ?".format(a - 4 * b, a - 3 * b, a - 2 * b, a - 1 * b)

    def solve(self, a, b):
        return a
