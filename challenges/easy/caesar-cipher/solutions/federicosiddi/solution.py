import string

low_letters = list(string.ascii_lowercase)
up_letters = list(string.ascii_uppercase)

def encode(original_sentence, shift):
    encoded_sentence = []
    for char in original_sentence:
        if char in low_letters:
            char_index = low_letters.index(char)
            encoded_sentence.append(low_letters[(char_index+shift)%26])
        elif char in up_letters:
            char_index = up_letters.index(char)
            encoded_sentence.append(up_letters[(char_index+shift)%26])
        else:
            encoded_sentence.append(char)
    return ''.join(encoded_sentence)

encoded_message = encode('Hello, World!', 7)
print(f"Encoded message: {encoded_message}")

def decode(original_sentence, shift):
    decoded_sentence = []
    for char in original_sentence:
        if char in low_letters:
            char_index = low_letters.index(char)
            decoded_sentence.append(low_letters[(char_index+(shift*-1))%26])
        elif char in up_letters:
            char_index = up_letters.index(char)
            decoded_sentence.append(up_letters[(char_index+(shift*-1))%26])
        else:
            decoded_sentence.append(char)
    return ''.join(decoded_sentence)

decoded_message = decode('CxvxaaxfMneb Axltb!', 9)
print(f"Decoded message: {decoded_message}")
