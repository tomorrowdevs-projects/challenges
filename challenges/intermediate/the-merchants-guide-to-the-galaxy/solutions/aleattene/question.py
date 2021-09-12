

def acquire_question(str_entered, all_values_settings_mapped_dict, multipliers_value, questions):
    """ This function acquires and stores the questions entered """
    # Conversion from string to list, using (space) separator
    lst_entered = str_entered.split(" ")
    # Entering of a question with incorrect structure (wrong number of parameters)
    if len(lst_entered) != 8:
        questions.append(["I have no idea what you are talking about"])
        return False
    # Question with the correct number of parameters, but with structure to be evaluated
    elif lst_entered[0] == "how" and lst_entered[7] == "?":
        # question that requires an answer in terms of numerical quantity
        if lst_entered[1] == "much" and lst_entered[2] == "is":
            for j in range(3, 7):
                if lst_entered[j] not in all_values_settings_mapped_dict:
                    # incorrect structure of the question
                    return False
                else:
                    # correct structure of the question
                    questions.append(lst_entered[3:7])
                    return True
        # question that requires an answer in terms of the number of credits
        elif lst_entered[1:4] == ["many", "Credits", "is"]:
            if lst_entered[4] in all_values_settings_mapped_dict and \
                    lst_entered[5] in all_values_settings_mapped_dict and \
                    lst_entered[6] in multipliers_value:
                # correct structure of the question
                questions.append(lst_entered[4:7])
                return True
            else:
                # incorrect structure of the question
                return False
    #  incorrect structure of the question
    return False
