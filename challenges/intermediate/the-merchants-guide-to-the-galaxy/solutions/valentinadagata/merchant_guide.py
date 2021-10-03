symbols = {"I" : 1, "V" : 5, "X" : 10, "L" : 50, "C" : 100, "D" : 500, "M" : 1000}
possible_verbs = ["is", "means"]
possible_questions = ["how much is", "how many Credits is"]

def valid_roman_number(num):
    """
    This function verify is the given number is a correct roman number
    with all the rules about repeated values and subtractions
    It returns True or False
    """
    error_message = ""
    # check wrong repetition in number
    limited_3 = ["X", "I", "C", "M"]
    limited_1 = ["D", "L", "V"]

    curr, cnt = None, 0

    for i in range(len(num)):
        # CHECK 1 : IS A ROMAN NUMBER
        if num[i] not in symbols:
            error_message = num[i] + " is not a roman number!"
            raise ValueError(error_message)
            return False

        # CHECK 2 : REPEATED CHARACTERS
        # increment similar character
        if num[i] == curr:
            cnt += 1
        else:
            curr, cnt = num[i], 1
        # if the count exceed lim and the character is among the ones that cannot be repeated
        if cnt > 1 and num[i] in limited_1:
            error_message = "The letter " + curr + " is repeated too many times consecutively (limit 1)"
            raise ValueError(error_message)
            return False
        # if the count exceed lim and the character is among the ones that cannot be repeated more than 3 times
        if cnt > 3 and num[i] in limited_3:
            error_message = "The letter " + curr + " is repeated too many times consecutively (limit 3)"
            raise ValueError(error_message)
            return False

        # CHECK 3: WHAT CAN BE SUBTRACTED
        if i < len(num) - 1:
            curr = num[i]
            next = num[i + 1]
            if symbols[curr] < symbols[next]:
                if curr not in limited_1:
                    if curr == "I" and (next == "V" or next == "X"):
                        return True
                    if curr == "X" and (next == "L" or next == "C"):
                        return True
                    if curr == "C" and (next == "D" or next == "M"):
                        return True
                return False
    return True


def let2num(roman):
    """
    This function takes the roman numbers, verify it with the valid_roman_number function and convert it in arab numbers
    It returns the converted number
    """
    roman = roman.upper()
    valid_roman_number(roman)
    num = 0
    i = 0
    while i in range(len(roman)):
        curr = roman[i]

        if i < len(roman) - 1:
            next = roman[i + 1]
            if (curr == "I" and (next == "V" or next == "X")) or (curr == "X" and (next == "L" or next == "C")) or (curr == "C" and (next == "D" or next == "M")):
                num += symbols[next] - symbols[curr]
                i += 1
            else:
                num += symbols[curr]
        else:
            num += symbols[curr]
        i += 1
    return num


def instructions_values(input_list):
    # this dictionary will be filled with the keys and the values es. "glob" : "I"
    values = {}
    # for those who use "is" and for those who use "means" in the instruction
    for instruction in input_list:
        divide_instruction = instruction.split()
        if len(divide_instruction) != 3:
            return False
        if divide_instruction[1] not in possible_verbs:
            return False

        # if the instruction input is valid, insert key and value into the dictionary
        if divide_instruction[0] not in values:
            values[divide_instruction[0]] = divide_instruction[2].upper()

    return values


def instruction_metals(input_list, input_metals):
    values = instructions_values(input_list)
    # this dictionary will be filled with the keys and the values es. "Silver" : "I"
    metals = {}

    # check if the metal input are correctly written
    for s in input_metals:
        val = 0  # this will be the value of the metal to be entered into the dictionary
        roman_num = "" # this will be the value to be converted

        split_string = s.split()
        # check for the "known" words i.e. Credits, is + the number
        if split_string[-1] != "Credits" or split_string[-2].isdigit() == False or split_string[-3] not in possible_verbs:
            return False

        # check if the remaining words are among the possible values
        # since I know that 4 words are always given (i.e. Silver is 34 Credits) i'll check for the others with a loop
        for i in range(len(split_string) - 4):
            if split_string[i] not in values:
                return False
            else:
                # calculate the value of the metal
                roman_num += str(values[split_string[i]])

        # convert roman to arab number
        val = let2num(roman_num)

        # save the name of the metals in the dictionary
        # this will be always in the -4 item of the splitted string
        if split_string[-4] not in metals:
            metals[split_string[-4]] = int(split_string[-2]) / val

    return metals


def check_question(input_list, input_metals, input_question):
    question = input_question.split()
    val = instructions_values(input_list)
    met = instruction_metals(input_list, input_metals)

    # insert here the words to calculate
    words = ""
    metals = ""
    # verify the question
    if question[1] == "much" and (question[0] + " " + question[1] + " " + question[2]) not in possible_questions:
        return False
    if question[1] == "many" and (question[0] + " " + question[1] + " " + question[2] + " " + question[3]) not in possible_questions:
        return False

    if question[1] == "much":
        # 3 words + ? are from the question
        for q in question[3:-1]:
            if q in val:
                words += q + " "
            elif q in met:
                metals += q + " "
            else:
                return False

    if question[1] == "many":
        # 4 words + ? are from the question
        for q in question[4:-1]:
            if q in val:
                words += q + " "
            elif q in met:
                metals += q
            else:
                return False

    return val, words, met, metals


def calculate_result(val, words, met, metals):
    roman = ""
    result = 0

    if words != "":
        for w in words.split():
            roman += val[w]

    num = let2num(roman)
    met_val = 1
    if metals != "":
        met_val = met[metals]
    result = num * met_val
    return result