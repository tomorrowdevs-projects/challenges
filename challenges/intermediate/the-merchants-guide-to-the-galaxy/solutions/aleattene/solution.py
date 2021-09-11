
"""
Python solution for challenge: "The Merchant's Guide to the Galaxy"
To start the tests, type from CLI: python tests.py
"""

from roman_number import *


def main():

    # Variables declaration
    num_first_input, num_second_input, num_questions = 4, 3, 5
    misunderstanding = "I'm sorry. I don't understand what you are saying to me."
    # Data structures declaration
    all_map_dict, multipliers_value, questions = {}, {}, []

    # Reception and control of the first information entered by the user
    for i in range(num_first_input):
        while True:
            # reception and control of the first information entered by the user
            str_entered = input("I'm wait: ")
            # control of the structure of the information entered
            if check_information_structure_first_setting(str_entered, all_map_dict):
                break
            else:
                print(misunderstanding)

    # Reception and control of the second information entered by the user
    for j in range(num_second_input):
        while True:
            str_entered = input("I'm still wait: ")
            # control of the structure of the information entered
            if check_information_structure_second_setting(str_entered, all_map_dict, multipliers_value):
                break
            else:
                print(misunderstanding)

    # Reception and storage of QUESTIONS entered by the user
    for k in range(num_questions):
        str_entered = input("Ask me the question: ")
        acquire_question(str_entered, all_map_dict, multipliers_value, questions)

    # Generation of ANSWERS to questions previously entered by the user
    for question in questions:
        print(generate_answer(question, all_map_dict, multipliers_value))


def check_information_structure_first_setting(str_entered, all_map_dict):
    """ This function ... """
    dict_roman_numbers = {
        "M": 1000,
        "D": 500,
        "C": 100,
        "L": 50,
        "X": 10,
        "V": 5,
        "I": 1
    }
    lst_entered = str_entered.split(" ")
    if len(lst_entered) != 3:
        return False
    if lst_entered[1] == "is" and lst_entered[2] in dict_roman_numbers:
        all_map_dict[lst_entered[0]] = lst_entered[2]
        return True
    else:
        return False


def check_information_structure_second_setting(str_entered, all_map_dict, multipliers_value):
    """ This function ... """
    allowed_symbols = ['M', 'D', 'C', 'L', 'X', 'V', 'I']
    lst_entered = str_entered.split(" ")
    if len(lst_entered) != 6:
        return False
    if lst_entered[0] in all_map_dict and lst_entered[1] in all_map_dict and \
            lst_entered[2] not in multipliers_value and lst_entered[3] == "is" and \
            lst_entered[4].isdigit() and lst_entered[5] == "Credits":
        roman_number = all_map_dict[lst_entered[0]] + all_map_dict[lst_entered[1]]
        if check_roman_number_correct_form(roman_number, allowed_symbols):
            multipliers_value[lst_entered[2]] = int(lst_entered[4]) / from_roman_number_to_integer(roman_number)
            return True
        else:
            return False
    else:
        return False


def acquire_question(str_entered, all_map_dict, multipliers_value, questions):
    """ This function ... """
    lst_entered = str_entered.split(" ")
    if len(lst_entered) != 8:
        questions.append(["I have no idea what you are talking about"])
        return False
    elif lst_entered[0] == "how" and lst_entered[7] == "?":
        if lst_entered[1] == "much" and lst_entered[2] == "is":
            for j in range(3, 7):
                if lst_entered[j] not in all_map_dict:
                    return False
                else:
                    questions.append(lst_entered[3:7])
                    return True
        elif lst_entered[1:4] == ["many", "Credits", "is"]:
            if lst_entered[4] in all_map_dict and lst_entered[5] in all_map_dict and \
                    lst_entered[6] in multipliers_value:
                questions.append(lst_entered[4:7])
                return True
    return False


def generate_answer(question, all_map_dict, multipliers_value):
    """ This function ... """
    allowed_symbols = ['M', 'D', 'C', 'L', 'X', 'V', 'I']
    roman_number = ""
    if len(question) == 4:
        for i in range(4):
            roman_number += all_map_dict[question[i]]
        if check_roman_number_correct_form(roman_number, allowed_symbols):
            number = from_roman_number_to_integer(roman_number)
            return " ".join(question) + " is " + str(number)
        else:
            return "I have no idea what you are talking about"
    elif len(question) == 3:
        for i in range(2):
            roman_number += all_map_dict[question[i]]
        if check_roman_number_correct_form(roman_number, allowed_symbols):
            number = from_roman_number_to_integer(roman_number)
            num_credits = int(number * multipliers_value[question[2]])
            return " ".join(question) + " is " + str(num_credits) + " Credits"
        else:
            return "I have no idea what you are talking about"
    else:
        return question[0]


if __name__ == "__main__":
    main()
