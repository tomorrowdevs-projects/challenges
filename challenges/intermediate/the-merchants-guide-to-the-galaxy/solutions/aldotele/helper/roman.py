import re


def roman_to_integer(roman):
    if not is_roman_valid(roman):
        raise ValueError("that's not a valid roman number")
    conversions = {"I": 1, "V": 5, "X": 10, "L": 50, "C": 100, "D": 500, "M": 1000}
    # BASE CASE
    # if there are no numeral left, I add zero to the sum and recursion ends
    if roman == '':
        return 0

    # if there is one numeral left, I add its value to the sum
    if len(roman) == 1:
        return conversions[roman]

    # if there are still two numerals, I convert them in integer in order to compare them
    preceding = conversions[roman[0]]
    following = conversions[roman[1]]

    # if the preceding is a higher value, I add it to the sum and call the function again from the following
    if preceding >= following:
        return preceding + roman_to_integer(roman[1:])
    # if the preceding is lower, I subtract it from the following and add the subtraction to the sum
    # then I call the function again but from the numeral which comes next to the following
    elif preceding < following:
        return (following - preceding) + roman_to_integer(roman[2:])


def is_roman_valid(string):
    # checks if the string is a roman number, e.g. "IV" is valid, "IVI" is not valid
    return True if re.search(r"^M{0,3}(CM|CD|D?C{0,3})(XC|XL|L?X{0,3})(IX|IV|V?I{0,3})$", string) else False


if __name__ == '__main__':
    r = "XXIVI"
    print(roman_to_integer(r))
