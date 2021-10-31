def caesar_cipher(message, shift):
# Process each character to construct the encrypted (or decrypted) message
    encrypted_message = ""
    for ch in message:
        if "a" <= ch <= "z":
            '''
            Process a lowercase letter by determining its
            position in the alphabet (0-25), computing its
            new position, and adding it to the new message
            '''
            pos = ord(ch) - ord("a")
            pos = (pos + shift) % 26
            new_char = chr(pos + ord("a"))
            encrypted_message += new_char
        elif "A" <= ch <= "Z":
            '''
            Process an uppercase letter by determining its
            position in the alphabet (0-25), computing its
            new position, and adding it to the new message
            '''
            pos = ord(ch) - ord("A")
            pos = (pos + shift) % 26
            new_char = chr(pos + ord("A"))
            encrypted_message += new_char
        else:
            # If the character is not a letter then copy it into the new message
            encrypted_message += ch
    
    return encrypted_message


def encode(shift):
    return shift


def decode(shift):
    return -1 * shift


def main():

    print("\nEncoded messages:")
    print(caesar_cipher('Hello, World!', encode(7)))
    print(caesar_cipher('I love pizza.', encode(-7)))
    print(caesar_cipher('HytyQapgnr kyicq qclqc. Qmkcrgkcq.', encode(50)))
    print(caesar_cipher('abc', encode(24)))

    print("\nDecoded messages:")
    print(caesar_cipher('CxvxaaxfMneb Axltb!', decode(9)))
    print(caesar_cipher('Gtdflw Defotz Nzop td rcple!!!', decode(-15)))
    print(caesar_cipher("Buj'i mhyju jxu syfxuh.", decode(120)))
    print(caesar_cipher('Vriwzduh Hqjlqhhulqj', decode(3)))


if __name__ == "__main__":
    main()


"""
Notes:
for negative number we have to understand the behavior of the modulus operator %
mod = n - (base * (n//base))

e.g. case where shift value is positive integer and the operation pos = ord(ch) - ord("a") generate a positive integer
2 - (97 * (2//97) ==> is the same as ==> 2 % 97 ==> both result is 2
then we'll add this value to ord("a") in order to find the correct position in the ASCII table

e.g. case where shift value is negative integer and the operation pos = ord(ch) - ord("a") generate a negative integer
-2 - (97 * (-2//97)) ==> is the same as ==> -2 % 97 ==> both result is 95
then we'll add this value to ord("a") in order to find the correct position in the ASCII table
"""