from helper.roman import roman_to_integer, is_roman_valid  # if it gives error try with "from .helper.roman"
import re


roman_units = {"I": 1, "V": 5, "X": 10, "L": 50, "C": 100, "D": 500, "M": 1000}
galaxy_units = {}
metals = {"SILVER": "", "GOLD": "", "IRON": ""}


def clean_input(s):
    # the function cleans the input to reduce the amount of validations needed
    s = re.sub(' +', ' ', s).upper().strip(".! ")  # removing extra space, side dots and making everything uppercase
    if s[-1] == "?" and s[-2] != " ":  # making sure there will be a space before the question mark
        s = s[:-1] + " " + s[-1]
    return s


def parse_input(s):
    """
    :param s: string
    :return: either an error or a function call
    """
    sl = s.split(" ")  # sl stands for string_as_list
    generic_error = "I have no idea what you are talking about"

    if len(sl) < 3 or "IS" not in sl:
        return print(generic_error)  # the input should always contain at least 3 words, among which the word "is"

    if len(sl) == 3:  # in this case it must be an input to train the machine
        conditions = [sl[0].isalpha(), sl[1] == "IS", sl[2] in roman_units]
        if all(conditions):
            return learn_galactic_to_roman(sl[0], sl[2])
        else:
            return print(generic_error)

    if len(sl) > 3:  # in this case it can be either a question for quantity or for metal credits
        conditions_a = [sl[-4] in metals, sl[-3] == "IS", sl[-2].isnumeric(), sl[-1] == "CREDITS"]  # training input
        conditions_b = [s.startswith("HOW MUCH IS "), s.endswith(" ?")]  # asking quantity
        conditions_c = [s.startswith("HOW MANY CREDITS IS "), s.endswith(" ?"), sl[-2] in metals]  # asking credits

        if all(conditions_a):  # e.g. "glob glob silver is 50 credits"
            try:
                return learn_metal_conversion(sl[:-4], sl[-4], sl[-2])  # learns the value of a metal unit
            except ValueError as e:
                return print(getattr(e, 'message', str(e)))

        elif all(conditions_b):  # e.g. "how much is glob glob prok ?"
            try:
                return tell_quantity(sl[3:-1])  # tells the arabic amount of the galactic quantity
            except ValueError as e:
                return print(getattr(e, 'message', str(e)))

        elif all(conditions_c):  # e.g. "how many credits is glob glob silver ?"
            try:
                return tell_credits(sl[4:-2], sl[-2])  # tells the credits of the galactic quantity of metal
            except ValueError as e:
                return print(getattr(e, 'message', str(e)))

        else:
            return print(generic_error)


def learn_galactic_to_roman(g, r):
    """
    :param g: string (single galaxy unit)
    :param r: string (roman base unit)
    :return: None
    """
    galaxy_units[g] = r


def galactic_to_roman(galactic_words):
    """
    :param galactic_words: a list of strings (galactic units)
    :return: string (roman number)
    """
    roman = ""
    for unit in galactic_words:
        if unit not in galaxy_units:
            if unit == galactic_words[-1] and unit in metals:
                raise ValueError("what? I think you mean how many credits...")
            raise ValueError("Never heard of this galactic quantity")
        roman += galaxy_units[unit]
    if not is_roman_valid(roman):
        raise ValueError("that's not a valid quantity")
    return roman


def learn_metal_conversion(galactic_words, metal, amount):
    """
    :param galactic_words: a list of strings (galactic units)
    :param metal: string (e.g. "Silver")
    :param amount: number of credits
    :return: None
    """
    arabic = roman_to_integer(galactic_to_roman(galactic_words))
    metal_value = int(amount) / arabic  # dividing the number of credits by the quantity of metal
    metals[metal] = metal_value  # storing the single metal value


def tell_quantity(galactic_words):
    """
    :param galactic_words: a list of strings (galactic units)
    :return: None
    """
    arabic = roman_to_integer(galactic_to_roman(galactic_words))
    print("%s is %d" % (' '.join(galactic_words), arabic))


def tell_credits(galactic_words, metal):
    """
    :param galactic_words: a list of strings (galactic units)
    :param metal: string
    :return: None
    """
    if not metals[metal]:
        raise ValueError("I do not know the value of that metal yet")
    arabic = roman_to_integer(galactic_to_roman(galactic_words))
    value = arabic * metals[metal]
    print("%s %s is %.2f Credits" % (' '.join(galactic_words), metal, value))


if __name__ == '__main__':
    while True:
        s = input("enter: ")
        if s != "":
            parse_input(clean_input(s))
        else:
            print("Bye bye...")
            break
    # print(galaxy_units)
    # print(metals)
