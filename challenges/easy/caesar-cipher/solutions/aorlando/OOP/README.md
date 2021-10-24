# Caesar Cipher

In cryptography, a Caesar cipher, also known as Caesar's cipher, the shift cipher, Caesar's code or Caesar shift, is one of the simplest and most widely known encryption techniques. It is a type of substitution cipher in which each letter in the plaintext is replaced by a letter some fixed number of positions down the alphabet. For example, with a left shift of `3`, `D` would be replaced by `A`, `E` would become `B`, and so on. The method is named after Julius Caesar, who used it in his private correspondence.

## Classes and caesar_cipher Package

The program is built using OOP approach.

`CaesarCipher` and `MessageVisualizer` represent the objects and they handle the following methods:

`CaesarCipher`
- `get_message()` - get the original message
- `set_lowercase_chars(char)` - process a lowercase letter
- `set_uppercase_chars(char)` - process a uppercase letter
- `encrypted_message()` - create the encrypted message
- `encode()` - handle if the user want to encode
- `decode()` - handle if the user want to decode

`MessageVisualizer`
- `print_ticket()` - return a fancy ticket with messages

```Python
"""
Expected Output with shift == 3

                                          ~
        +======================================================================+
        |                          Caesar Cipher Algo                          |
        +======================================================================+
        |                        Original message: ciao                        |
        |                       Encrypted message: fldr                        |
        +======================================================================+
                                          ~
"""
```


