from unittest import TestCase
from decimal import *
from operations import round


class TestRound(TestCase):

    def test_solve_ten_half(self):
        r = round.Round()
        r.a = Decimal('145')
        r.b = 10
        s = r.solve()
        self.assertEqual(s, 150)

    def test_solve_ten_up(self):
        r = round.Round()
        r.a = Decimal('149')
        r.b = 10
        s = r.solve()
        self.assertEqual(s, 150)

    def test_solve_ten_down(self):
        r = round.Round()
        r.a = Decimal('142')
        r.b = 10
        s = r.solve()
        self.assertEqual(s, 140)

    def test_solve_hundred_half(self):
        r = round.Round()
        r.a = Decimal('150')
        r.b = 100
        s = r.solve()
        self.assertEqual(s, 200)

    def test_solve_hundred_up(self):
        r = round.Round()
        r.a = Decimal('176')
        r.b = 100
        s = r.solve()
        self.assertEqual(s, 200)

    def test_solve_hundred_down(self):
        r = round.Round()
        r.a = Decimal('122')
        r.b = 100
        s = r.solve()
        self.assertEqual(s, 100)
