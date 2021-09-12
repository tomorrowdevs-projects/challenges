

def roman_number_generator(arabic_number):
    """ This function converts an arabic number (int) into a roman number (str) """
    roman_numbers_symbol_value = [
        ("M", 1000), ("CM", 900), ("D", 500), ("CD", 400),
        ("C", 100), ("XC", 90), ("L", 50), ("XL", 40), ("XXX", 30), ("XX", 20),
        ("X", 10), ("IX", 9), ("V", 5), ("IV", 4), ("I", 1)]
    roman_num = ""
    for symbol, value in roman_numbers_symbol_value:
        while arabic_number >= value:
            arabic_number -= value
            roman_num += symbol
    return roman_num


def check_roman_number_correct_form(roman_num, roman_numbers_allowed_symbols_list, symbol_occurrences_no_repeat=0,
                                    symbol_occurrences=0, symbol_previous="M", roman_num_backup=""):
    """ This function checks the structural consistency of a roman number """
    # Data structures declaration
    roman_numbers_dict = {
        "M": 1000,
        "D": 500,
        "C": 100,
        "L": 50,
        "X": 10,
        "V": 5,
        "I": 1
    }
    roman_numbers_four_symbols_combinations = [
        'MMMCM', 'CCCXC', 'XXXIX'
    ]
    roman_numbers_next_allowed_symbols_dict = {
        "M": ['M', 'D', 'C', 'L', 'X', 'V', 'I'],
        "D": ['C', 'L', 'X', 'V', 'I'],
        "C": ['M', 'D', 'C', 'L', 'X', 'V', 'I'],
        "L": ['X', 'V', 'I'],
        "X": ['C', 'L', 'X', 'V', 'I'],
        "V": ['I'],
        "I": ['X', 'V', 'I']
    }
    # Handling of function parameters/arguments
    if not roman_num:
        return False
    if not symbol_occurrences:
        symbol_occurrences = {
            'M': 0,
            'C': 0,
            'X': 0,
            'I': 0
        }
    if not symbol_occurrences_no_repeat:
        symbol_occurrences_no_repeat = {
            'V': 0,
            'L': 0,
            'D': 0
        }
    # First symbol
    symbol = roman_num[0]
    # Backup for the management of occurrences
    roman_num_backup = roman_num_backup + symbol
    # Possible updating of symbols that can repeat themselves (M, C, X, I)
    if symbol in symbol_occurrences:
        symbol_occurrences[symbol] += 1
        # each symbol can appear at most three times (consecutively) or four (roman_numbers_four_symbols_combinations)
        if symbol_occurrences[symbol] > 4:
            return False
        elif symbol_occurrences[symbol] == 4:
            for combination in roman_numbers_four_symbols_combinations:
                if combination in roman_num_backup:
                    break
                else:
                    continue
    # Possible updating of symbols that cannot be repeated (D, V, L)
    elif symbol in symbol_occurrences_no_repeat:
        symbol_occurrences_no_repeat[symbol] += 1
        if symbol_occurrences_no_repeat[symbol] > 1:
            return False
    # Base Case (only the last symbol remains to be evaluated)
    if len(roman_num) == 1:
        if symbol in roman_numbers_allowed_symbols_list:
            return True
        else:
            return False
    # Recursive case (all other symbols of the roman number except the first)
    tail = roman_num[1:]
    # Check if the symbol is valid (it must be among those allowed by the previous symbol)
    if symbol in roman_numbers_allowed_symbols_list:
        # check if the value of the current symbol is higher than the previous one
        if roman_numbers_dict[symbol] > roman_numbers_dict[symbol_previous]:
            # index of the previous symbol in the list of subsequent symbols allowed by the current symbol
            index_previous = roman_numbers_next_allowed_symbols_dict[symbol].index(symbol_previous)
            # checks whether or not it is possible to return to a list of allowed symbols
            if index_previous + 1 == len(roman_numbers_next_allowed_symbols_dict[symbol]):
                roman_numbers_allowed_symbols_list = []
            else:
                # list of symbols allowed by the current symbol, filtered according to the previous symbol
                roman_numbers_allowed_symbols_list = roman_numbers_next_allowed_symbols_dict[symbol][index_previous + 1:]
            # recursive call
            return True and check_roman_number_correct_form(tail, roman_numbers_allowed_symbols_list,
                                                            symbol_occurrences_no_repeat, symbol_occurrences,
                                                            symbol, roman_num_backup)
        # in this case, the value of the current symbol is less than or equal to the the previous one
        else:
            # check if the symbol is one of the symbols that cannot be repeated (D, V, L)
            if symbol_previous in symbol_occurrences_no_repeat:
                if symbol_previous in roman_numbers_next_allowed_symbols_dict[symbol]:
                    # index of the previous symbol in the list of subsequent symbols allowed by the current symbol
                    index_previous = roman_numbers_next_allowed_symbols_dict[symbol].index(symbol_previous)
                    # list of symbols allowed by the current symbol, filtered according to the previous symbol
                    roman_numbers_allowed_symbols_list = \
                        roman_numbers_next_allowed_symbols_dict[symbol][index_previous + 1:]
                else:
                    # list of symbols allowed by the current symbol
                    roman_numbers_allowed_symbols_list = roman_numbers_next_allowed_symbols_dict[symbol]
                # recursive call
                return True and check_roman_number_correct_form(tail, roman_numbers_allowed_symbols_list,
                                                                symbol_occurrences_no_repeat, symbol_occurrences,
                                                                symbol, roman_num_backup)
            else:
                # list of symbols allowed by the current symbol
                roman_numbers_allowed_symbols_list = roman_numbers_next_allowed_symbols_dict[symbol]
                # recursive call
                return True and check_roman_number_correct_form(tail, roman_numbers_allowed_symbols_list,
                                                                symbol_occurrences_no_repeat, symbol_occurrences,
                                                                symbol, roman_num_backup)
    else:
        # incorrect structure of the roman number
        return False


def from_roman_number_to_integer(roman_num):
    """ This function converts a roman number (str) into an arabic number (int)"""
    roman_numbers_dict = {
        "M": 1000,
        "D": 500,
        "C": 100,
        "L": 50,
        "X": 10,
        "V": 5,
        "I": 1
    }
    # Base case (only the last symbol remains to be evaluated)
    if len(roman_num) == 1:
        return roman_numbers_dict[roman_num]
    # Recursive case (all other symbols of the roman number except the first)
    tail = roman_num[1:len(roman_num)]
    # Decimal value of the first symbol
    current_value = roman_numbers_dict[roman_num[0]]
    # Comparison of present value with previous value
    if current_value >= roman_numbers_dict[roman_num[1]]:
        # present value greater or equal than previous value
        return current_value + from_roman_number_to_integer(tail)
    else:
        # present value less than previous value
        return -current_value + from_roman_number_to_integer(tail)
