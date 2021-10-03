from re import search


# the class bot defines what the bot can do and store items and metals
class Bot:

    # @input is broken in two parts: prefix and suffix.
    # @items and metals stored from input entered by user
    def __init__(self, prefix: str = '', suffix: str = '', items: dict = dict(), metals: dict = dict()):
        self.prefix = prefix
        self.suffix = suffix.replace("?", "")
        self.items = items
        self.metals = metals

    # converts roman-type string in int using recursion
    def roman2int(self, roman: str) -> int:
        romans_table = {'M': 1000, 'D': 500, 'C': 100, 'L': 50, 'X': 10, 'V': 5, 'I': 1}

        roman = roman.upper()

        # base condition
        if roman == '':
            return 0

        if roman[0] not in romans_table:
            raise KeyError

        if len(roman) > 1:
            # check the syntax to find IV, IX, ecc.
            if romans_table[roman[0]] < romans_table[roman[1]]:
                tot = romans_table[roman[1]] - romans_table[roman[0]]
                return tot + self.roman2int(roman[2:])

        tot = romans_table[roman[0]]

        return tot + self.roman2int(roman[1:])

    # define a single unit adding it in the dict items
    def checkUnits(self):
        self.items[self.prefix] = self.suffix.upper()

        return "{} = {}\n".format(self.prefix.strip(), self.roman2int(self.suffix))

    # store the value of this metal
    def checkMetal(self):

        # find the value in credits
        total_credits = float(search(r"\d+", self.suffix).group())

        # split the prefix and find the metal as the last element in the list
        quantity_list = self.prefix.split()
        new_metal = quantity_list.pop()

        # convert the remaining element in roman-symbols, concatenate in one unique string | Now convert it in number
        total_items = self.roman2int("".join([self.items[x] for x in quantity_list]))

        # define a new metal and its value
        self.metals[new_metal] = round(total_credits / total_items, 2)

        return "Ok now the price of {} is {}!\n".format(new_metal.capitalize(), self.metals[new_metal])

    # sums units entered by user
    def unitSum(self):

        # split suffix in singles elements (ex. "pish tegj glob glob" in ["pish", "tegj", "glob", "glob"]
        quantity_list = self.suffix.split()

        # convert every element in its roman-symbols and concatenate in one unique string | Now convert it in number
        total_items = self.roman2int("".join([self.items[x] for x in quantity_list]))

        return "{} is {}\n".format(self.suffix.strip(), total_items)

    # calculate the value in credits of a quantity of a metal
    def countMetal(self):

        # split the prefix and find the metal as the last element in the list
        quantity_list = self.suffix.split()
        metal = quantity_list.pop()

        # convert every element in its roman-symbols and concatenate in one unique string | Now convert it in number
        total_items = self.roman2int("".join([self.items[x] for x in quantity_list]))

        if metal not in self.metals.keys():

            return "Metal not found!"

        else:

            return "{} is {} Credits\n".format(self.suffix.strip(), self.metals[metal] * total_items)
