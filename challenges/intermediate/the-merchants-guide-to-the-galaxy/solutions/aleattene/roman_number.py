

def roman_number_generator(number):
    """ This function converts an arabic number (int) into a roman number (str) """
    symbols_value = [
        ("M", 1000), ("CM", 900), ("D", 500), ("CD", 400),
        ("C", 100), ("XC", 90), ("L", 50), ("XL", 40), ("XXX", 30), ("XX", 20),
        ("X", 10), ("IX", 9), ("V", 5), ("IV", 4), ("I", 1)]
    result = ""
    for symbol, value in symbols_value:
        while number >= value:
            number -= value
            result += symbol
    return result


def check_roman_number_correct_form(roman_number, allowed_symbols, symbol_occurrences_no_repeat=0,
                                    symbol_occurrences=0, symbol_previous="M", number_backup=""):
    """ This function checks the structural consistency of a roman number """
    """ The code works correctly but it is absolutely necessary to refactor it"""
    roman_numbers_dict = {
        "M": 1000,
        "D": 500,
        "C": 100,
        "L": 50,
        "X": 10,
        "V": 5,
        "I": 1
    }
    roman_numbers_four_combinations = ['MMMCM', 'CCCXC', 'XXXIX']
    roman_numbers_smaller_dict = {
        "M": ['M', 'D', 'C', 'L', 'X', 'V', 'I'],
        "D": ['C', 'L', 'X', 'V', 'I'],
        "C": ['M', 'D', 'C', 'L', 'X', 'V', 'I'],
        "L": ['X', 'V', 'I'],
        "X": ['C', 'L', 'X', 'V', 'I'],
        "V": ['I'],
        "I": ['X', 'V', 'I']
    }
    if not roman_number:
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
    # print(allowed_symbols)
    # print("number: " + roman_number)
    # First symbol
    symbol = roman_number[0]
    number_backup = number_backup + symbol
    if symbol in symbol_occurrences:
        symbol_occurrences[symbol] += 1
        # print(symbol_occurrences[symbol])
        if symbol_occurrences[symbol] > 4:
            return False
        elif symbol_occurrences[symbol] == 4:
            for combination in roman_numbers_four_combinations:
                # print(combination)
                # print(number_backup)
                if combination in number_backup:
                    break
                else:
                    continue
    elif symbol in symbol_occurrences_no_repeat:
        symbol_occurrences_no_repeat[symbol] += 1
        if symbol_occurrences_no_repeat[symbol] > 1:
            return False
    # print("current symbol: " + symbol)
    if len(roman_number) == 1:
        if symbol in allowed_symbols:
            return True
        else:
            return False
    # Remaining symbols
    tail = roman_number[1:]
    if symbol in allowed_symbols:
        # print(roman_numbers_dict[symbol])
        # print(symbol_previous)
        # print(roman_numbers_dict[symbol_previous])
        if roman_numbers_dict[symbol] > roman_numbers_dict[symbol_previous]:
            index_previous = roman_numbers_smaller_dict[symbol].index(symbol_previous)
            # print(index_previous)
            if index_previous + 1 == len(roman_numbers_smaller_dict[symbol]):
                allowed_symbols = []
            else:
                allowed_symbols = roman_numbers_smaller_dict[symbol][index_previous + 1:]
            return True and check_roman_number_correct_form(tail, allowed_symbols,
                                                            symbol_occurrences_no_repeat, symbol_occurrences,
                                                            symbol, number_backup)
        else:
            if symbol_previous in symbol_occurrences_no_repeat:
                if symbol_previous in roman_numbers_smaller_dict[symbol]:
                    index_previous = roman_numbers_smaller_dict[symbol].index(symbol_previous)
                    allowed_symbols = roman_numbers_smaller_dict[symbol][index_previous + 1:]
                else:
                    allowed_symbols = roman_numbers_smaller_dict[symbol]
                return True and check_roman_number_correct_form(tail, allowed_symbols,
                                                                symbol_occurrences_no_repeat, symbol_occurrences,
                                                                symbol, number_backup)
            else:
                allowed_symbols = roman_numbers_smaller_dict[symbol]
                return True and check_roman_number_correct_form(tail, allowed_symbols,
                                                                symbol_occurrences_no_repeat, symbol_occurrences,
                                                                symbol, number_backup)
    else:
        return False


def from_roman_number_to_integer(roman_number):
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
    # Base case
    if len(roman_number) == 1:
        return roman_numbers_dict[roman_number]
    # Recursive case (each recursive case remove first char of the tail)
    tail = roman_number[1:len(roman_number)]
    # Decimal value of the first char of the list
    current_value = roman_numbers_dict[roman_number[0]]
    # Comparison of present value with previous value
    if current_value >= roman_numbers_dict[roman_number[1]]:
        # present value greater or equal than previous value
        return current_value + from_roman_number_to_integer(tail)
    else:
        # present value less than previous value
        return -current_value + from_roman_number_to_integer(tail)


if __name__ == "__main__":
    for i in range(1, 1):
        roman_number = roman_number_generator(i)
        allowed_symbols = ['M', 'D', 'C', 'L', 'X', 'V', 'I']
        # roman_number = ""
        print(f'{roman_number} = ', end="")
        print(check_roman_number_correct_form(roman_number, allowed_symbols))
