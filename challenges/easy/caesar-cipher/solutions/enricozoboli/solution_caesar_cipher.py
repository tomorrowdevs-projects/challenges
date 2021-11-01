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
    decoded_word = ""
    for char in word:
        if 97 <= ord(char) <= 122:
            decoded_word += chr((((ord(char) - ord("a")) - shift) % 26) 
            + ord("a"))
        elif 65 <= ord(char) <= 90:
            decoded_word += chr((((ord(char) - ord("A")) - shift) % 26) 
            + ord("A"))
        else:
            decoded_word += char

    return decoded_word

print(encode('Hello, World!', 7))                      # => 'Olssv, Dvysk!'
print(encode('I love pizza.', -7))                      # => 'B ehox ibsst.'
print(encode('HytyQapgnr kyicq qclqc. Qmkcrgkcq.', 50)) # => 'HytyQapgnr kyicq qclqc. Qmkcrgkcq.'
print(encode('abc', 24))                                # => 'yza'

print(decode('CxvxaaxfMneb Axltb!', 9))                 # => 'TomorrowDevs Rocks!'
print(decode('Gtdflw Defotz Nzop td rcple!!!', -15))    # => 'Visual Studio Code is great!!!'
print(decode("Buj'i mhyju jxu syfxuh.", 120))           # => 'Let's write the cipher.'
print(decode('Vriwzduh Hqjlqhhulqj', 3))                # => 'Software Engineering'
