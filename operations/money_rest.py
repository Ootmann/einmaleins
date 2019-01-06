from operations import abstract_operation


class MoneyRest(abstract_operation.AbstractOperation):

    def __init__(self):
        super().__init__("money_rest", "Restgeld berechnen")

    def get_question(self, a, b):
        return "Du bezahlst {} € mit einem {} € Schein. Rückgeld?".format(str(a).replace('.', ','), b)

    def solve(self, a, b):
        return '{0:.2f}'.format(b - a).replace('.', ',') + " €"
