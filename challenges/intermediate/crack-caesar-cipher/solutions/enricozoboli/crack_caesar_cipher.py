import encode_decode

with open("cases/Shakespeare-Macbeth.txt") as file_1,\
    open("cases/Shakespeare-Hamlet.txt") as file_2,\
    open(("cases/Shakespeare-Romeo-And-Juliet.txt")) as file_3 :
    books = [file_2.read(), file_1.read(), file_3.read()]

def english_frequent_letter():
    """
    This function calculate the most frequent character in the english 
    language based on https://en.wikipedia.org/wiki/Letter_frequency.
    """
    #The dictionary was shamelessly copied and pasted from aleattene's solution 
    frequency_dict = {
        'a': 8.167, 'b': 1.492, 'c': 2.782, 'd': 4.253, 'e': 12.702, 
        'f': 2.228, 'g': 2.015, 'h': 6.094, 'i': 6.966, 'j': 0.153, 
        'k': 0.772, 'l': 4.025, 'm': 2.406, 'n': 6.749, 'o': 7.507, 
        'p': 1.929, 'q': 0.095, 'r': 5.987, 's': 6.327, 't': 9.056, 
        'u': 2.758, 'v': 0.978, 'w': 2.360, 'x': 0.150, 'y': 1.974, 'z': 0.074
    }
    max_freq_values = max(frequency_dict.values())
    most_frequent_letter = [k for k,v in frequency_dict.items()
    if v == max_freq_values]
    return most_frequent_letter

def build_character_dict(b):
    """
    This function  build a frequency dictionary 
    with every characters of the encripted text.
    """
    d = {}
    for l in b:
        if l in d and  33 <= ord(l) <= 126:
            d[l] += 1
        else:
            if 33 <= ord(l) <= 126:
                d[l] = 1
    encoded_char_dictionary = d
    return encoded_char_dictionary

def calculate_shift(b):
    """
    This function determine the most frequent characters in the
    encripted text and compute the shift comparing the character frequency 
    """
    all_values = build_character_dict(b).values()
    max_values = max(all_values)
    most_rep_letter = [k for k,v in build_character_dict(b).items() 
    if v == max_values]
    shift = ord(most_rep_letter[0]) - ord(english_frequent_letter()[0])
    return shift

def main():
    for i in range(0,len(books)):
        print(encode_decode.decode(books[i], calculate_shift(books[i])))
        print("\n" * 2)

if __name__ == "__main__" :
    main()