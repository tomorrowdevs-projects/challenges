
import re


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


def roman_number_is_valid(roman_num):
    """ This function checks the structural consistency of a roman number using a regular expression
            M{0,3} -> <empty>, M, MM, MMM
            CM|CD|D?C{0,3} -> <empty>, C, CC, CCC, CD, D, DC, DCC, DCCC, CM
            XC|XL|L?X{0,3} -> <empty>, X, XX, XXX, XL, L, LX, LXX, LXXX, XC
            IX|IV|V?I{0,3} -> <empty>, I, II, III, IV, V, VI, VII, VIII, IX
    """
    if re.search(r"^M{0,3}(CM|CD|D?C{0,3})(XC|XL|L?X{0,3})(IX|IV|V?I{0,3})$", roman_num):
        return True
    else:
        return False


def from_roman_number_to_integer(roman_num):
    """ This function converts a roman number (str) into an arabic number (int)"""
    roman_numbers_dict = {"M": 1000, "D": 500, "C": 100, "L": 50, "X": 10, "V": 5, "I": 1}
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
