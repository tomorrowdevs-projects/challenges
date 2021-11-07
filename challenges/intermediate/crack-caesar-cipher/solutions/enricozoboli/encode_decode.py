def encode(word, shift):
    encoded_word = ""
    for char in word:
        if 97 <= ord(char) <= 122:
            encoded_word += chr((((ord(char) - ord("a")) + shift) % 26) 
            + ord("a"))
        elif 65 <= ord(char) <= 90:
            encoded_word += chr((((ord(char) - ord("A")) + shift) % 26) 
            + ord("A"))
        else:
            encoded_word += char

    return encoded_word

def decode(word, shift):
    return encode(word, -shift)
