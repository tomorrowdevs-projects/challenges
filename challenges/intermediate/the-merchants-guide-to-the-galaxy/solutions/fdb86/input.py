from re import search
from bot import Bot


class InputBot:

    def __init__(self, prefix: str = '', suffix: str = ''):
        self.prefix = prefix
        self.suffix = suffix
        self.bot = Bot(prefix=self.prefix, suffix=self.suffix)

    def __str__(self):

        return "{}\n{}".format(self.bot.items, self.bot.metals)

    # manage the input entered by the user
    def checkInput(self):
        if len(self.suffix) == 1 and self.bot.roman2int(self.suffix) > 0:

            return self.bot.checkUnits()

        elif self.prefix == "how much":

            return self.bot.unitSum()

        elif self.prefix == "how many credits":

            return self.bot.countMetal()

        elif search(r"credits\Z", self.suffix):

            return self.bot.checkMetal()

        else:

            return "Value not in Roman Table!\n"
