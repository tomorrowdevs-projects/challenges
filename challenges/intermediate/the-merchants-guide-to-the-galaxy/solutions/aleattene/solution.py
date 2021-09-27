
"""
Python solution for challenge: "The Merchant's Guide to the Galaxy"
To start the tests, type from CLI: python tests.py
"""

from helper import *
from question import acquire_question
from answer import generate_answer


def main():
    # Variables declaration
    num_first_settings = 4
    num_second_settings = 3
    num_questions = 5
    # Data structures declaration
    all_values_settings_mapped_dict = {}
    multipliers_value = {}
    questions = []

    # Reception and control of the information setting entered by the user
    print("\nPlease, enter the basic settings:")
    for i in range(num_first_settings + num_second_settings):
        while True:
            # reception and control of the information entered by the user
            str_entered = input("-> ")
            # control of the structure of the information entered
            if (i < num_first_settings and first_setting_is_valid(str_entered, all_values_settings_mapped_dict)) \
                or (num_first_settings <= i < num_second_settings
                    and second_setting_is_valid(str_entered, all_values_settings_mapped_dict, multipliers_value)):
                break
            else:
                print("I'm sorry. I don't understand what you are saying to me.")

    # Reception and storage of QUESTIONS entered by the user
    print("\nNow, ask me the questions:")
    for _ in range(num_questions):
        str_entered = input("-> ")
        acquire_question(str_entered, all_values_settings_mapped_dict, multipliers_value, questions)

    # Generation of ANSWERS to questions previously entered by the user
    print("\nWell, the answers to your questions are as follows:")
    for question in questions:
        print("-> ", end="")
        print(generate_answer(question, all_values_settings_mapped_dict, multipliers_value))


if __name__ == "__main__":
    main()
