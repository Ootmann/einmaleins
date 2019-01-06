from operations import abstract_operation


class MoneyAdd(abstract_operation.AbstractOperation):

    def __init__(self):
        super().__init__("money_add", "Geld zusammenzählen")

    def get_question(self, a, b):
        return "{} € + {} €".format(a, b).replace('.', ',')

    def solve(self, a, b):
        return '{0:.2f}'.format(a + b).replace('.', ',') + " €"
