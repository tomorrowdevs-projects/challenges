

def acquire_question(str_entered, all_values_settings_mapped_dict, multipliers_value, questions):
    """ This function ... """
    lst_entered = str_entered.split(" ")
    if len(lst_entered) != 8:
        questions.append(["I have no idea what you are talking about"])
        return False
    elif lst_entered[0] == "how" and lst_entered[7] == "?":
        if lst_entered[1] == "much" and lst_entered[2] == "is":
            for j in range(3, 7):
                if lst_entered[j] not in all_values_settings_mapped_dict:
                    return False
                else:
                    questions.append(lst_entered[3:7])
                    return True
        elif lst_entered[1:4] == ["many", "Credits", "is"]:
            if lst_entered[4] in all_values_settings_mapped_dict and \
                    lst_entered[5] in all_values_settings_mapped_dict and \
                    lst_entered[6] in multipliers_value:
                questions.append(lst_entered[4:7])
                return True
    return False
