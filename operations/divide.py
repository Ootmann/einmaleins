from operations import abstract_operation


class Divide(abstract_operation.AbstractOperation):

    def __init__(self):
        super().__init__(":", "Teilen")

    def get_question(self, a, b):
        return "{} : {}".format(str(a), str(b))

    def solve(self, a, b):
        return int(a / b)
