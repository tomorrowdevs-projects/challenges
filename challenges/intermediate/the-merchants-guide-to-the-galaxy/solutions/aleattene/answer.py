

from roman_number import *


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
