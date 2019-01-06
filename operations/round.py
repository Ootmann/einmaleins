from operations import abstract_operation


class Round(abstract_operation.AbstractOperation):

    def __init__(self):
        super().__init__("round", "Runden")

    def get_question(self, a, b):
        if b == -1:
            return "{} auf den nächsten Zehner runden".format(a)
        elif b == -2:
            return "{} auf den nächsten Hunderter runden".format(a)

    def solve(self, a, b):
        return int(round(a, b))
