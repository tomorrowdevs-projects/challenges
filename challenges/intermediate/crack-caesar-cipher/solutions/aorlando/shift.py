from data_cleaning import DataCleaning


class Shift:

    """
    This class represents the shift value passed from the user by Crack class
    and processed it to return a list of possible shift values by using
    the difference_between_ascii_chars() method.
    """

    # vowels is ordered by relative frequency in the English language
    # reference: https://en.wikipedia.org/wiki/Letter_frequency
    list_of_vowels = ["e", "a", "o", "i", "u", "y"]
    
    def get_ascii_index(self):
        ascii_indexes = {}
        for letter in self.list_of_vowels:
            ascii_indexes[letter] = ord(letter)
        return ascii_indexes
    

    def difference_between_ascii_chars(self, char):
        list_of_diff = []
        ascii_index = self.get_ascii_index()
        for index in ascii_index:
            diff = ascii_index[index] - ord(char)
            list_of_diff.append(diff)
        return list_of_diff



# TEST
def main():
    FNAME1 = "Shakespeare-Hamlet.txt"
    test = DataCleaning(FNAME1)
    test1 = Shift()

    print(test1.get_ascii_index())
    print(test1.difference_between_ascii_chars("z"))

if __name__ == "__main__":
    main()
