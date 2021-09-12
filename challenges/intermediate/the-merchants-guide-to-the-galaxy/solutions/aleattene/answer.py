

from roman_number import *


def generate_answer(question, roman_numbers_allowed_symbols_list, all_values_settings_mapped_dict, multipliers_value):
    """ This function generates an answer based on the question received """
    roman_num = ""
    # Checks if you need to generate an answer to a question with a three or four parameter
    if len(question) == 4:
        for j in range(4):
            roman_num += all_values_settings_mapped_dict[question[j]]
        # check if the structure of the question (and therefore the corresponding roman number) is correct
        if check_roman_number_correct_form(roman_num, roman_numbers_allowed_symbols_list):
            # generation of the corresponding arabic number and therefore also of the correct answer
            arabic_number = from_roman_number_to_integer(roman_num)
            return " ".join(question) + " is " + str(arabic_number)
        else:
            # incorrect question structure
            return "I have no idea what you are talking about"
    elif len(question) == 3:
        for k in range(2):
            roman_num += all_values_settings_mapped_dict[question[k]]
        # check if the structure of the question (and therefore the corresponding roman number) is correct
        if check_roman_number_correct_form(roman_num, roman_numbers_allowed_symbols_list):
            # generation of the corresponding arabic number and therefore also of the correct answer
            arabic_number = from_roman_number_to_integer(roman_num)
            num_credits = int(arabic_number * multipliers_value[question[2]])
            return " ".join(question) + " is " + str(num_credits) + " Credits"
        else:
            # incorrect question structure
            return "I have no idea what you are talking about"
    else:
        # incorrect question structure
        return question[0]
