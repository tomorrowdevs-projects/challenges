
""" To start the tests, type from CLI: python tests.py """

import unittest
from solution import *
from roman_number import *


class TestSolution(unittest.TestCase):

    def test_first_settings_acquisitions(self):
        print("\nTEST FIRST SETTING")
        all_values_settings_mapped_dict = {}
        # glob
        self.assertEqual(first_setting_is_valid('glob is I', all_values_settings_mapped_dict), True)
        self.assertEqual(first_setting_is_valid('glob is I', all_values_settings_mapped_dict),
                         all_values_settings_mapped_dict['glob'] == 'I')
        self.assertEqual(first_setting_is_valid('glob is is I',
                                                all_values_settings_mapped_dict), False)
        self.assertEqual(first_setting_is_valid('glob slob is I',
                                                all_values_settings_mapped_dict), False)
        self.assertEqual(first_setting_is_valid('glob is I I',
                                                all_values_settings_mapped_dict), False)
        # prok
        self.assertEqual(first_setting_is_valid('prok is V', all_values_settings_mapped_dict), True)
        self.assertEqual(first_setting_is_valid('prok is V', all_values_settings_mapped_dict),
                         all_values_settings_mapped_dict['prok'] == 'V')
        self.assertEqual(first_setting_is_valid('prok is is V',
                                                all_values_settings_mapped_dict), False)
        self.assertEqual(first_setting_is_valid('prok prok is V',
                                                all_values_settings_mapped_dict), False)
        self.assertEqual(first_setting_is_valid('prok is V V',
                                                all_values_settings_mapped_dict), False)
        # pish
        self.assertEqual(first_setting_is_valid('pish is X', all_values_settings_mapped_dict), True)
        self.assertEqual(first_setting_is_valid('pish is X', all_values_settings_mapped_dict),
                         all_values_settings_mapped_dict['pish'] == 'X')
        self.assertEqual(first_setting_is_valid('pish is is X',
                                                all_values_settings_mapped_dict), False)
        self.assertEqual(first_setting_is_valid('pish pish is X',
                                                all_values_settings_mapped_dict), False)
        self.assertEqual(first_setting_is_valid('pish is X X',
                                                all_values_settings_mapped_dict), False)
        # tegj
        self.assertEqual(first_setting_is_valid('tegj is L', all_values_settings_mapped_dict), True)
        self.assertEqual(first_setting_is_valid('tegj is L', all_values_settings_mapped_dict),
                         all_values_settings_mapped_dict['tegj'] == 'L')
        self.assertEqual(first_setting_is_valid('tegj is is L',
                                                all_values_settings_mapped_dict), False)
        self.assertEqual(first_setting_is_valid('tegj tegj is L',
                                                all_values_settings_mapped_dict), False)
        self.assertEqual(first_setting_is_valid('tegj is L L',
                                                all_values_settings_mapped_dict), False)
        self.assertEqual(all_values_settings_mapped_dict, {'glob': 'I', 'prok': 'V', 'pish': 'X', 'tegj': 'L'})
        print("TEST FIRST SETTING - OK")

    def test_second_settings_acquisitions(self):
        print("\nTEST SECOND SETTING")
        all_values_settings_mapped_dict = {'glob': 'I', 'prok': 'V', 'pish': 'X', 'tegj': 'L'}
        multipliers_value = {}
        # glob glob Silver
        self.assertEqual(second_setting_is_valid(
            'glob glob Silver is 34 Credits', all_values_settings_mapped_dict, multipliers_value),
            multipliers_value['Silver'] == 17.0)
        self.assertEqual(second_setting_is_valid(
            'glob glob Silver is 34 Credits', all_values_settings_mapped_dict, multipliers_value), False)
        self.assertEqual(second_setting_is_valid(
            'glob glob glob Silver is 34 Credits', all_values_settings_mapped_dict, multipliers_value), False)
        self.assertEqual(second_setting_is_valid(
            'glob glob Silver Silver is 34 Credits', all_values_settings_mapped_dict, multipliers_value), False)
        self.assertEqual(second_setting_is_valid(
            'glob glob Silver is is 34 Credits', all_values_settings_mapped_dict, multipliers_value), False)
        self.assertEqual(second_setting_is_valid(
            'glob glob Silver is 34.0 Credits', all_values_settings_mapped_dict, multipliers_value), False)
        self.assertEqual(second_setting_is_valid(
            'glob glob Silver is 34 credits', all_values_settings_mapped_dict, multipliers_value), False)
        # glob glob Gold
        self.assertEqual(second_setting_is_valid(
            'glob prok Gold is 57800 Credits', all_values_settings_mapped_dict, multipliers_value),
            multipliers_value['Gold'] == 14450.0)
        self.assertEqual(second_setting_is_valid(
            'glob prok Gold is 57800 Credits', all_values_settings_mapped_dict, multipliers_value), False)
        self.assertEqual(second_setting_is_valid(
            'glob prok Gold Gold is 57800 Credits', all_values_settings_mapped_dict, multipliers_value), False)
        self.assertEqual(second_setting_is_valid(
            'glob prok Gold Gold is 57800 Credits', all_values_settings_mapped_dict, multipliers_value), False)
        self.assertEqual(second_setting_is_valid(
            'glob prok Gold is is 57800 Credits', all_values_settings_mapped_dict, multipliers_value), False)
        self.assertEqual(second_setting_is_valid(
            'glob prok Gold is 57800.0 Credits', all_values_settings_mapped_dict, multipliers_value), False)
        self.assertEqual(second_setting_is_valid(
            'glob prok Gold is 57800 credits', all_values_settings_mapped_dict, multipliers_value), False)
        # pish pish Iron
        self.assertEqual(second_setting_is_valid(
            'pish pish Iron is 3910 Credits', all_values_settings_mapped_dict, multipliers_value),
            multipliers_value['Iron'] == 195.5)
        self.assertEqual(second_setting_is_valid(
            'pish pish Iron is 3910 Credits', all_values_settings_mapped_dict, multipliers_value), False)
        self.assertEqual(second_setting_is_valid(
            'pish pish pish Iron is 3910 Credits', all_values_settings_mapped_dict, multipliers_value), False)
        self.assertEqual(second_setting_is_valid(
            'pish pish Iron Iron is 3910 Credits', all_values_settings_mapped_dict, multipliers_value), False)
        self.assertEqual(second_setting_is_valid(
            'pish pish Iron is is 3910 Credits', all_values_settings_mapped_dict, multipliers_value), False)
        self.assertEqual(second_setting_is_valid(
            'pish pish Iron is 3910.0 Credits', all_values_settings_mapped_dict, multipliers_value), False)
        self.assertEqual(second_setting_is_valid(
            'pish pish Iron is 3910 credits', all_values_settings_mapped_dict, multipliers_value), False)
        self.assertEqual(multipliers_value, {'Silver': 17.0, 'Gold': 14450.0, 'Iron': 195.5})
        print("TEST SECOND SETTING - OK")

    def test_questions_acquired(self):
        print("\nTEST QUESTIONS")
        all_values_settings_mapped_dict = {'glob': 'I', 'prok': 'V', 'pish': 'X', 'tegj': 'L'}
        multipliers_value = {'Silver': 17.0, 'Gold': 14450.0, 'Iron': 195.5}
        questions = []
        self.assertEqual(acquire_question(
            "how much is pish tegj glob glob ?", all_values_settings_mapped_dict, multipliers_value, questions),
            questions[0] == ["pish", "tegj", "glob", "glob"])
        self.assertEqual(acquire_question(
            "how many Credits is glob prok Silver ?", all_values_settings_mapped_dict, multipliers_value, questions),
            questions[1] == ["glob", "prok", "Silver"])
        self.assertEqual(acquire_question(
            "how many Credits is glob prok Gold ?", all_values_settings_mapped_dict, multipliers_value, questions),
            questions[2] == ["glob", "prok", "Gold"])
        self.assertEqual(acquire_question(
            "how many Credits is glob prok Iron ?", all_values_settings_mapped_dict, multipliers_value, questions),
            questions[3] == ["glob", "prok", "Iron"])
        self.assertEqual(acquire_question(
            "how much wood could a woodchuck chuck if a woodchuck could chuck wood ?",
            all_values_settings_mapped_dict, multipliers_value, questions),
            questions[4] == "I have no idea what you are talking about")
        self.assertEqual(questions, [
            ["pish", "tegj", "glob", "glob"],
            ["glob", "prok", "Silver"],
            ["glob", "prok", "Gold"],
            ["glob", "prok", "Iron"],
            ["I have no idea what you are talking about"]])
        print("TEST QUESTIONS - OK")

    def test_answers_generated(self):
        print("\nTEST ANSWERS")
        all_values_settings_mapped_dict = {'glob': 'I', 'prok': 'V', 'pish': 'X', 'tegj': 'L'}
        multipliers_value = {'Silver': 17.0, 'Gold': 14450.0, 'Iron': 195.5}
        questions = [
            ["pish", "tegj", "glob", "glob"],
            ["glob", "prok", "Silver"],
            ["glob", "prok", "Gold"],
            ["glob", "prok", "Iron"],
            ["I have no idea what you are talking about"]]
        self.assertEqual(generate_answer(
            questions[0], all_values_settings_mapped_dict, multipliers_value), "pish tegj glob glob is 42")
        self.assertEqual(generate_answer(
            questions[1], all_values_settings_mapped_dict, multipliers_value), "glob prok Silver is 68 Credits")
        self.assertEqual(generate_answer(
            questions[2], all_values_settings_mapped_dict, multipliers_value), "glob prok Gold is 57800 Credits")
        self.assertEqual(generate_answer(
            questions[3], all_values_settings_mapped_dict, multipliers_value), "glob prok Iron is 782 Credits")
        self.assertEqual(generate_answer(
            questions[4], all_values_settings_mapped_dict, multipliers_value),
            "I have no idea what you are talking about")
        print("TEST ANSWERS - OK")

    def test_conversions_from_roman_number_to_integer(self):
        print("\nTEST CONVERSION ROMAN NUMBER - INTEGER NUMBER")
        for arabic_number in range(1, 4000):
            self.assertEqual(from_roman_number_to_integer(roman_number_generator(arabic_number)), arabic_number)
        self.assertEqual(from_roman_number_to_integer("MMVI"), 2006)
        self.assertEqual(from_roman_number_to_integer("MCMXLIV"), 1944)
        self.assertEqual(from_roman_number_to_integer("I"), 1)
        self.assertEqual(from_roman_number_to_integer("V"), 5)
        self.assertEqual(from_roman_number_to_integer("X"), 10)
        self.assertEqual(from_roman_number_to_integer("VIII"), 8)
        self.assertEqual(from_roman_number_to_integer("MMMCMXCIX"), 3999)
        self.assertEqual(from_roman_number_to_integer("IX"), 9)
        self.assertEqual(from_roman_number_to_integer("XL"), 40)
        self.assertEqual(from_roman_number_to_integer("XCIX"), 99)
        self.assertEqual(from_roman_number_to_integer("LXXXIX"), 89)
        self.assertEqual(from_roman_number_to_integer("XXXIX"), 39)
        self.assertEqual(from_roman_number_to_integer("XXVIII"), 28)
        self.assertEqual(from_roman_number_to_integer("MMMCMXCIX"), 3999)
        self.assertEqual(from_roman_number_to_integer("III"), 3)
        self.assertEqual(from_roman_number_to_integer("XXX"), 30)
        self.assertEqual(from_roman_number_to_integer("CCC"), 300)
        self.assertEqual(from_roman_number_to_integer("CCCXC"), 390)
        self.assertEqual(from_roman_number_to_integer("MMM"), 3000)
        self.assertEqual(from_roman_number_to_integer("MMMCM"), 3900)
        print("TEST CONVERSION ROMAN NUMBER - INTEGER NUMBER - OK")

    def test_check_roman_number_correct_form(self):
        print("\nTEST STRUCTURE ROMAN NUMBER")
        for arabic_number in range(1, 4000):
            # print(roman_number_generator(arabic_number))
            self.assertEqual(roman_number_is_valid(roman_number_generator(arabic_number)), True)
        self.assertEqual(roman_number_is_valid("DLMXII"), False)
        self.assertEqual(roman_number_is_valid("MCCXIVL"), False)
        self.assertEqual(roman_number_is_valid("CMXLVIX"), False)
        self.assertEqual(roman_number_is_valid("MDCLVXI"), False)
        self.assertEqual(roman_number_is_valid("IVCDLXC"), False)
        self.assertEqual(roman_number_is_valid("MMMXLIVI"), False)
        self.assertEqual(roman_number_is_valid("IXXXILI"), False)
        self.assertEqual(roman_number_is_valid("DLXXVIL"), False)
        self.assertEqual(roman_number_is_valid("CLCXIV"), False)
        self.assertEqual(roman_number_is_valid("MXIXV"), False)
        self.assertEqual(roman_number_is_valid("MXIX"), True)
        self.assertEqual(roman_number_is_valid("LIXI"), False)
        self.assertEqual(roman_number_is_valid("LIX"), True)
        self.assertEqual(roman_number_is_valid("VIXI"), False)
        self.assertEqual(roman_number_is_valid("VIXI"), False)
        self.assertEqual(roman_number_is_valid("XIX"), True)
        self.assertEqual(roman_number_is_valid("MIM"), False)
        self.assertEqual(roman_number_is_valid("MIMM"), False)
        self.assertEqual(roman_number_is_valid("MMM"), True)
        self.assertEqual(roman_number_is_valid("DCM"), False)
        self.assertEqual(roman_number_is_valid("LXC"), False)
        self.assertEqual(roman_number_is_valid("VIC"), False)
        self.assertEqual(roman_number_is_valid("IIII"), False)
        self.assertEqual(roman_number_is_valid("VVVV"), False)
        self.assertEqual(roman_number_is_valid("XXXX"), False)
        self.assertEqual(roman_number_is_valid("LLLL"), False)
        self.assertEqual(roman_number_is_valid("CCCC"), False)
        self.assertEqual(roman_number_is_valid("DDDD"), False)
        self.assertEqual(roman_number_is_valid("MMMM"), False)

        print("TEST STRUCTURE ROMAN NUMBER - OK")


if __name__ == '__main__':
    """ The following instruction executes the tests
    by discovering all classes present in this file
    that inherit from unittest.TestCase.
    """
    unittest.main()
