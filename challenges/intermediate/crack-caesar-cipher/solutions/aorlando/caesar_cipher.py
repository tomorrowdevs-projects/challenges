class CaesarCipher:

    """
    This class represents the main algorithm used for
    decoding the message with Caesar Cipher strategy.
    It takes the message and the shift value passed from Crack 
    class by the user input and then processed it with decrypt() method
    """

    def __init__(self, message, shift=0):
        self.message = message
        self.shift = shift
    

    def set_lowercase_chars(self, char):
        '''
        Process a lowercase letter by determining its
        position in the alphabet (0-25), computing its
        new position, and adding it to the new message
        '''
        if "a" <= char <= "z":
            pos = ord(char) - ord("a")
            pos = (pos + self.shift) % 26
            lowercase_char = chr(pos + ord("a"))
        else:
            return False

        return lowercase_char


    def set_uppercase_chars(self, char):
        '''
        Process an uppercase letter by determining its
        position in the alphabet (0-25), computing its
        new position, and adding it to the new message
        '''
        if "A" <= char <= "Z":
            pos = ord(char) - ord("A")
            pos = (pos + self.shift) % 26
            uppercase_char = chr(pos + ord("A"))
        else:
            return False

        return uppercase_char


    def decrypt(self):
        new_message = ""
        for ch in self.message:
            if self.set_lowercase_chars(ch):
                new_message += self.set_lowercase_chars(ch)
            elif self.set_uppercase_chars(ch):
                new_message += self.set_uppercase_chars(ch)
            else:
                # If the character is not a letter then copy it into the new message
                new_message += ch
           
        return new_message


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
