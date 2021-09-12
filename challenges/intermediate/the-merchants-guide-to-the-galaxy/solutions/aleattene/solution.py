
"""
Python solution for challenge: "The Merchant's Guide to the Galaxy"
To start the tests, type from CLI: python tests.py
"""

from helper import *
from question import acquire_question
from answer import generate_answer


def main():
    # Variables declaration
    num_first_settings, num_second_settings, num_questions = 4, 3, 5
    misunderstanding = "I'm sorry. I don't understand what you are saying to me."
    # Data structures declaration
    all_values_settings_mapped_dict, multipliers_value, questions = {}, {}, []
    roman_numbers_allowed_symbols_list = ['M', 'D', 'C', 'L', 'X', 'V', 'I']

    # Reception and control of the first information entered by the user
    for _ in range(num_first_settings):
        while True:
            # reception and control of the first information entered by the user
            str_entered = input("I'm wait: ")
            # control of the structure of the information entered
            if check_information_structure_first_setting(str_entered, all_values_settings_mapped_dict):
                break
            else:
                print(misunderstanding)

    # Reception and control of the second information entered by the user
    for _ in range(num_second_settings):
        while True:
            str_entered = input("I'm still wait: ")
            # control of the structure of the information entered
            if check_information_structure_second_setting(str_entered, roman_numbers_allowed_symbols_list,
                                                          all_values_settings_mapped_dict, multipliers_value):
                break
            else:
                print(misunderstanding)

    # Reception and storage of QUESTIONS entered by the user
    for _ in range(num_questions):
        str_entered = input("Ask me the question: ")
        acquire_question(str_entered, all_values_settings_mapped_dict, multipliers_value, questions)

    # Generation of ANSWERS to questions previously entered by the user
    for question in questions:
        print(generate_answer(question, roman_numbers_allowed_symbols_list,
                              all_values_settings_mapped_dict, multipliers_value))


if __name__ == "__main__":
    main()
