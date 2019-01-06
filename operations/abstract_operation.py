from abc import ABC, abstractmethod


class AbstractOperation(ABC):

    def __init__(self, sign, description):
        self.sign = sign
        self.description = description
        super().__init__()

    @abstractmethod
    def get_question(self, a, b):
        pass

    @abstractmethod
    def solve(self, a, b):
        pass
