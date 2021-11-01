def encode(word, shift):
    """
    This function take a string and a shift amount and return a
    new string in wich each charter is replaced by another one
    according to the Caesar Cipher technique.
    """  
    
    if word == "":
        return  word
    else:
        if 97 <= ord(word[0]) <= 122:
            encoded_char = chr((((ord(word[0]) - ord("a")) + shift) % 26) 
                + ord("a"))
            return encoded_char + encode(word[1:], shift)
        elif 65 <= ord(word[0]) <= 90:
            encoded_char = chr((((ord(word[0]) - ord("A")) + shift) % 26) 
                + ord("A"))
            return encoded_char + encode(word[1:], shift)
        else :
            return word[0] + encode(word[1:], shift)


def decode(word, shift):
    return encode(word, -shift)


print(encode('Hello, World!', 7))                      # => 'Olssv, Dvysk!'
print(encode('I love pizza.', -7))                      # => 'B ehox ibsst.'
print(encode('HytyQapgnr kyicq qclqc. Qmkcrgkcq.', 50)) # => 'HytyQapgnr kyicq qclqc. Qmkcrgkcq.'
print(encode('abc', 24))                                # => 'yza'

print(decode('CxvxaaxfMneb Axltb!', 9))                 # => 'TomorrowDevs Rocks!'
print(decode('Gtdflw Defotz Nzop td rcple!!!', -15))    # => 'Visual Studio Code is great!!!'
print(decode("Buj'i mhyju jxu syfxuh.", 120))           # => 'Let's write the cipher.'
print(decode('Vriwzduh Hqjlqhhulqj', 3))                # => 'Software Engineering'
