alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
alphabet_upper = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
punctuation_marks = ['!', '"', '%', '&', '/', '(', ')', '=', '?', '^', '+', "'", '-', ' ']

def encode(enc,numb):
    new_string = ""
    for i in enc:
        if i in punctuation_marks:
            new_string += i
        elif i in alphabet_upper:
            new_string += alphabet_upper[(alphabet_upper.index(i) + numb) % 26]
        elif i in alphabet:
            new_string += alphabet[(alphabet.index(i) + numb) % 26]
    return new_string

print(encode('Hello, world!', 7))

def decode(enc,numb):
    new_string = ""
    for i in enc:
        if i in punctuation_marks:
            new_string += i
        elif i in alphabet_upper:
            new_string += alphabet_upper[(alphabet_upper.index(i) + numb) % - 26]
        elif i in alphabet:
            new_string += alphabet[(alphabet.index(i) + numb) % - 26]
    return new_string

print(decode('Olssv dvysk!', -7))