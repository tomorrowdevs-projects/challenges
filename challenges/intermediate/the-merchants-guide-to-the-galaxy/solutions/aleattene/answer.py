

from roman_number import *


def generate_answer(question, roman_numbers_allowed_symbols_list, all_values_settings_mapped_dict, multipliers_value):
    """ This function ... """
    roman_num = ""
    if len(question) == 4:
        for j in range(4):
            roman_num += all_values_settings_mapped_dict[question[j]]
        if check_roman_number_correct_form(roman_num, roman_numbers_allowed_symbols_list):
            arabic_number = from_roman_number_to_integer(roman_num)
            return " ".join(question) + " is " + str(arabic_number)
        else:
            return "I have no idea what you are talking about"
    elif len(question) == 3:
        for k in range(2):
            roman_num += all_values_settings_mapped_dict[question[k]]
        if check_roman_number_correct_form(roman_num, roman_numbers_allowed_symbols_list):
            arabic_number = from_roman_number_to_integer(roman_num)
            num_credits = int(arabic_number * multipliers_value[question[2]])
            return " ".join(question) + " is " + str(num_credits) + " Credits"
        else:
            return "I have no idea what you are talking about"
    else:
        return question[0]
