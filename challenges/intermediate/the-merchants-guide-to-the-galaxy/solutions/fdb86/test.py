import unittest
from input import InputBot
from bot import Bot


class TestInputBot(unittest.TestCase):

    def test_checkUnits(self):
        prefix, suffix = "glob is I".split(" is ")
        robot_test = InputBot(prefix=prefix, suffix=suffix)
        self.assertEqual(robot_test.checkInput(), "glob = 1\n")

    def test_checheckMetal(self):
        items = {'glob': 'I'}
        prefix, suffix = "glob glob Silver is 34 Credits".split(" is ")
        robot_test = Bot(prefix=prefix, suffix=suffix, items=items)
        self.assertEqual(robot_test.checkMetal(), "Ok now the price of Silver is 17.0!\n")

    def test_unitSum(self):
        items = {'glob': 'I', 'prok': 'V', 'pish': 'X', 'tegj': 'L'}
        prefix, suffix = "how much is pish tegj glob glob ?".split(" is ")
        robot_test = Bot(prefix=prefix, suffix=suffix, items=items)
        self.assertEqual(robot_test.unitSum(), "pish tegj glob glob is 42\n")

    def test_countMetal(self):
        items = {'glob': 'I', 'prok': 'V', 'pish': 'X', 'tegj': 'L'}
        metals = {'silver': 34, 'gold': 57800, 'iron': 195.5}
        prefix, suffix = "how many Credits is glob prok iron ?".split(" is ")
        robot_test = Bot(prefix=prefix, suffix=suffix, items=items, metals=metals)
        self.assertEqual(robot_test.countMetal(), "glob prok iron is 782.0 Credits\n")