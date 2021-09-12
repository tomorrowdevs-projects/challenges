
""" To start the tests, type from CLI: python tests.py """

import unittest
from solution import *
from roman_number import *


class TestSolution(unittest.TestCase):

    def test_first_settings_acquisitions(self):
        print("\nTEST FIRST SETTING")
        all_values_settings_mapped_dict = {}
        # glob
        self.assertEqual(check_information_structure_first_setting('glob is I',
                                                                   all_values_settings_mapped_dict), True)
        self.assertEqual(check_information_structure_first_setting('glob is I',
                                                                   all_values_settings_mapped_dict),
                         all_values_settings_mapped_dict['glob'] == 'I')
        self.assertEqual(check_information_structure_first_setting('glob is is I',
                                                                   all_values_settings_mapped_dict), False)
        self.assertEqual(check_information_structure_first_setting('glob slob is I',
                                                                   all_values_settings_mapped_dict), False)
        self.assertEqual(check_information_structure_first_setting('glob is I I',
                                                                   all_values_settings_mapped_dict), False)
        # prok
        self.assertEqual(check_information_structure_first_setting('prok is V',
                                                                   all_values_settings_mapped_dict), True)
        self.assertEqual(check_information_structure_first_setting('prok is V',
                                                                   all_values_settings_mapped_dict),
                         all_values_settings_mapped_dict['prok'] == 'V')
        self.assertEqual(check_information_structure_first_setting('prok is is V',
                                                                   all_values_settings_mapped_dict), False)
        self.assertEqual(check_information_structure_first_setting('prok prok is V',
                                                                   all_values_settings_mapped_dict), False)
        self.assertEqual(check_information_structure_first_setting('prok is V V',
                                                                   all_values_settings_mapped_dict), False)
        # pish
        self.assertEqual(check_information_structure_first_setting('pish is X',
                                                                   all_values_settings_mapped_dict), True)
        self.assertEqual(check_information_structure_first_setting('pish is X',
                                                                   all_values_settings_mapped_dict),
                         all_values_settings_mapped_dict['pish'] == 'X')
        self.assertEqual(check_information_structure_first_setting('pish is is X',
                                                                   all_values_settings_mapped_dict), False)
        self.assertEqual(check_information_structure_first_setting('pish pish is X',
                                                                   all_values_settings_mapped_dict), False)
        self.assertEqual(check_information_structure_first_setting('pish is X X',
                                                                   all_values_settings_mapped_dict), False)
        # tegj
        self.assertEqual(check_information_structure_first_setting('tegj is L',
                                                                   all_values_settings_mapped_dict), True)
        self.assertEqual(check_information_structure_first_setting('tegj is L',
                                                                   all_values_settings_mapped_dict),
                         all_values_settings_mapped_dict['tegj'] == 'L')
        self.assertEqual(check_information_structure_first_setting('tegj is is L',
                                                                   all_values_settings_mapped_dict), False)
        self.assertEqual(check_information_structure_first_setting('tegj tegj is L',
                                                                   all_values_settings_mapped_dict), False)
        self.assertEqual(check_information_structure_first_setting('tegj is L L',
                                                                   all_values_settings_mapped_dict), False)
        self.assertEqual(all_values_settings_mapped_dict, {'glob': 'I', 'prok': 'V', 'pish': 'X', 'tegj': 'L'})
        print("TEST FIRST SETTING - OK")

    def test_second_settings_acquisitions(self):
        print("\nTEST SECOND SETTING")
        all_values_settings_mapped_dict = {'glob': 'I', 'prok': 'V', 'pish': 'X', 'tegj': 'L'}
        roman_numbers_allowed_symbols_list = ['M', 'D', 'C', 'L', 'X', 'V', 'I']
        multipliers_value = {}
        # glob glob Silver
        self.assertEqual(check_information_structure_second_setting(
            'glob glob Silver is 34 Credits', roman_numbers_allowed_symbols_list,
            all_values_settings_mapped_dict, multipliers_value), multipliers_value['Silver'] == 17.0)
        self.assertEqual(check_information_structure_second_setting(
            'glob glob Silver is 34 Credits', roman_numbers_allowed_symbols_list,
            all_values_settings_mapped_dict, multipliers_value), False)
        self.assertEqual(check_information_structure_second_setting(
            'glob glob glob Silver is 34 Credits', roman_numbers_allowed_symbols_list,
            all_values_settings_mapped_dict, multipliers_value), False)
        self.assertEqual(check_information_structure_second_setting(
            'glob glob Silver Silver is 34 Credits', roman_numbers_allowed_symbols_list,
            all_values_settings_mapped_dict, multipliers_value), False)
        self.assertEqual(check_information_structure_second_setting(
            'glob glob Silver is is 34 Credits', roman_numbers_allowed_symbols_list,
            all_values_settings_mapped_dict, multipliers_value), False)
        self.assertEqual(check_information_structure_second_setting(
            'glob glob Silver is 34.0 Credits', roman_numbers_allowed_symbols_list,
            all_values_settings_mapped_dict, multipliers_value), False)
        self.assertEqual(check_information_structure_second_setting(
            'glob glob Silver is 34 credits', roman_numbers_allowed_symbols_list,
            all_values_settings_mapped_dict, multipliers_value), False)
        # glob glob Gold
        self.assertEqual(check_information_structure_second_setting(
            'glob prok Gold is 57800 Credits', roman_numbers_allowed_symbols_list,
            all_values_settings_mapped_dict, multipliers_value),
            multipliers_value['Gold'] == 14450.0)
        self.assertEqual(check_information_structure_second_setting(
            'glob prok Gold is 57800 Credits', roman_numbers_allowed_symbols_list,
            all_values_settings_mapped_dict, multipliers_value), False)
        self.assertEqual(check_information_structure_second_setting(
            'glob prok Gold Gold is 57800 Credits', roman_numbers_allowed_symbols_list,
            all_values_settings_mapped_dict, multipliers_value), False)
        self.assertEqual(check_information_structure_second_setting(
            'glob prok Gold Gold is 57800 Credits', roman_numbers_allowed_symbols_list,
            all_values_settings_mapped_dict, multipliers_value), False)
        self.assertEqual(check_information_structure_second_setting(
            'glob prok Gold is is 57800 Credits', roman_numbers_allowed_symbols_list,
            all_values_settings_mapped_dict, multipliers_value), False)
        self.assertEqual(check_information_structure_second_setting(
            'glob prok Gold is 57800.0 Credits', roman_numbers_allowed_symbols_list,
            all_values_settings_mapped_dict, multipliers_value), False)
        self.assertEqual(check_information_structure_second_setting(
            'glob prok Gold is 57800 credits', roman_numbers_allowed_symbols_list,
            all_values_settings_mapped_dict, multipliers_value), False)
        # pish pish Iron
        self.assertEqual(check_information_structure_second_setting(
            'pish pish Iron is 3910 Credits', roman_numbers_allowed_symbols_list,
            all_values_settings_mapped_dict, multipliers_value),
            multipliers_value['Iron'] == 195.5)
        self.assertEqual(check_information_structure_second_setting(
            'pish pish Iron is 3910 Credits', roman_numbers_allowed_symbols_list,
            all_values_settings_mapped_dict, multipliers_value), False)
        self.assertEqual(check_information_structure_second_setting(
            'pish pish pish Iron is 3910 Credits', roman_numbers_allowed_symbols_list,
            all_values_settings_mapped_dict, multipliers_value), False)
        self.assertEqual(check_information_structure_second_setting(
            'pish pish Iron Iron is 3910 Credits', roman_numbers_allowed_symbols_list,
            all_values_settings_mapped_dict, multipliers_value), False)
        self.assertEqual(check_information_structure_second_setting(
            'pish pish Iron is is 3910 Credits', roman_numbers_allowed_symbols_list,
            all_values_settings_mapped_dict, multipliers_value), False)
        self.assertEqual(check_information_structure_second_setting(
            'pish pish Iron is 3910.0 Credits', roman_numbers_allowed_symbols_list,
            all_values_settings_mapped_dict, multipliers_value), False)
        self.assertEqual(check_information_structure_second_setting(
            'pish pish Iron is 3910 credits', roman_numbers_allowed_symbols_list,
            all_values_settings_mapped_dict, multipliers_value), False)
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
        roman_numbers_allowed_symbols_list = ['M', 'D', 'C', 'L', 'X', 'V', 'I']
        all_values_settings_mapped_dict = {'glob': 'I', 'prok': 'V', 'pish': 'X', 'tegj': 'L'}
        multipliers_value = {'Silver': 17.0, 'Gold': 14450.0, 'Iron': 195.5}
        questions = [
            ["pish", "tegj", "glob", "glob"],
            ["glob", "prok", "Silver"],
            ["glob", "prok", "Gold"],
            ["glob", "prok", "Iron"],
            ["I have no idea what you are talking about"]]
        self.assertEqual(generate_answer(
            questions[0], roman_numbers_allowed_symbols_list, all_values_settings_mapped_dict, multipliers_value),
            "pish tegj glob glob is 42")
        self.assertEqual(generate_answer(
            questions[1], roman_numbers_allowed_symbols_list, all_values_settings_mapped_dict, multipliers_value),
            "glob prok Silver is 68 Credits")
        self.assertEqual(generate_answer(
            questions[2], roman_numbers_allowed_symbols_list, all_values_settings_mapped_dict, multipliers_value),
            "glob prok Gold is 57800 Credits")
        self.assertEqual(generate_answer(
            questions[3], roman_numbers_allowed_symbols_list, all_values_settings_mapped_dict, multipliers_value),
            "glob prok Iron is 782 Credits")
        self.assertEqual(generate_answer(
            questions[4], roman_numbers_allowed_symbols_list, all_values_settings_mapped_dict, multipliers_value),
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
        roman_numbers_allowed_symbols_list = ['M', 'D', 'C', 'L', 'X', 'V', 'I']
        for arabic_number in range(1, 4000):
            # print(roman_number_generator(arabic_number))
            self.assertEqual(check_roman_number_correct_form(roman_number_generator(arabic_number),
                                                             roman_numbers_allowed_symbols_list), True)
        self.assertEqual(check_roman_number_correct_form("DLMXII", roman_numbers_allowed_symbols_list), False)
        self.assertEqual(check_roman_number_correct_form("MCCXIVL", roman_numbers_allowed_symbols_list), False)
        self.assertEqual(check_roman_number_correct_form("CMXLVIX", roman_numbers_allowed_symbols_list), False)
        self.assertEqual(check_roman_number_correct_form("MDCLVXI", roman_numbers_allowed_symbols_list), False)
        self.assertEqual(check_roman_number_correct_form("IVCDLXC", roman_numbers_allowed_symbols_list), False)
        self.assertEqual(check_roman_number_correct_form("MMMXLIVI", roman_numbers_allowed_symbols_list), False)
        self.assertEqual(check_roman_number_correct_form("IXXXILI", roman_numbers_allowed_symbols_list), False)
        self.assertEqual(check_roman_number_correct_form("DLXXVIL", roman_numbers_allowed_symbols_list), False)
        self.assertEqual(check_roman_number_correct_form("CLCXIV", roman_numbers_allowed_symbols_list), False)
        self.assertEqual(check_roman_number_correct_form("MXIXV", roman_numbers_allowed_symbols_list), False)
        self.assertEqual(check_roman_number_correct_form("MXIX", roman_numbers_allowed_symbols_list), True)
        self.assertEqual(check_roman_number_correct_form("LIXI", roman_numbers_allowed_symbols_list), False)
        self.assertEqual(check_roman_number_correct_form("LIX", roman_numbers_allowed_symbols_list), True)
        self.assertEqual(check_roman_number_correct_form("VIXI", roman_numbers_allowed_symbols_list), False)
        self.assertEqual(check_roman_number_correct_form("VIXI", roman_numbers_allowed_symbols_list), False)
        self.assertEqual(check_roman_number_correct_form("XIX", roman_numbers_allowed_symbols_list), True)
        self.assertEqual(check_roman_number_correct_form("MIM", roman_numbers_allowed_symbols_list), False)
        self.assertEqual(check_roman_number_correct_form("MIMM", roman_numbers_allowed_symbols_list), False)
        self.assertEqual(check_roman_number_correct_form("MMM", roman_numbers_allowed_symbols_list), True)
        self.assertEqual(check_roman_number_correct_form("DCM", roman_numbers_allowed_symbols_list), False)
        self.assertEqual(check_roman_number_correct_form("LXC", roman_numbers_allowed_symbols_list), False)
        self.assertEqual(check_roman_number_correct_form("VIC", roman_numbers_allowed_symbols_list), False)
        print("TEST STRUCTURE ROMAN NUMBER - OK")


if __name__ == '__main__':
    """ The following instruction executes the tests
    by discovering all classes present in this file
    that inherit from unittest.TestCase.
    """
    unittest.main()
