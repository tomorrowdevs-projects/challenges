# Crack the Caesar Cipher Algo

In cryptography, a Caesar cipher, also known as Caesar's cipher, the shift cipher, Caesar's code or Caesar shift, is one of the simplest and most widely known encryption techniques. It is a type of substitution cipher in which each letter in the plaintext is replaced by a letter some fixed number of positions down the alphabet. For example, with a left shift of `3`, `D` would be replaced by `A`, `E` would become `B`, and so on. The method is named after Julius Caesar, who used it in his private correspondence.

#### *but.. what if someone want to crack this algorithm and find a way to decrypt every secret messages??* 👀

The scope of this program is to find a way for decrypting every secred messages passed as file, by using input from the user on CLI.

The program is built using OOP approach.

# Classes and methods of crack_caesar_cipher package

### `Crack`
- `quit_program(istruction)` - quit the program by eneter istruction "q"
- `show_files()` - show all the files in the cases folder
- `get_file(file_id)` - return the `file_id` entered by the user and return the file name
- `parse_shift()` - return the exact shift value that `CaesarCipher` class needs
- `make_file(decode_file)` - take the entire message decrypted and make a new file at decoded-files folder
- `path_for_decoded_files()` - return the path to decoded-files folder


### `CaesarCipher`
- `set_lowercase_chars(char)` - process a lowercase letter
- `set_uppercase_chars(char)` - process a uppercase letter
- `encrypted_message()` - create the encrypted message

### `DataCleaning`
- `get_path()` - get the pat of cases folder
- `get_dict_of_files()` - make a dict of all files inside cases folder
- `read_file()` - read the entire file
- `read_only_500_lines()` - read only the first 500 lines of the file
- `frequency_of_values()` - return what is the most frequent chars finded in the original encrypted file
- `most_common_letter()` - return the most common letter occurred from `frequency_of_values()` method

### `Shift`
- `get_ascii_index()` - get the ascii index of vowels ordered by relative frequency in the English language
- `difference_between_ascii_chars(char)` - return a list of possible shift values by computing: `ascii_index[self.get_ascii_index()] - ord(char)`

# CLI

The business logic of the program is handled by the `Crack` class. This class manage input and output and guide the user through the program.

Input scheme syntax:

- Istruction: start with ">>> "
- Error message: "ERROR: <error message>"
- Description: "DESCRIPTION: <description message>"


The program ask if the preview of the decrypted message is right and once the input from the user is positive, then the program create a file decrypted and place it at the decoded-files folder.

# How to Launch
First clone this repo on your local machine. The entry point is `main.py` script, so digit from CLI `$ python3 main.py` for mac, or `$ py main.py` for windows.
The program will guide you to all the steps.

In the cases folder you'll find some sample of encrypted file in order to test the program. If you want decrypting another text, add your .txt file in the cases folder and re-lounch the program.


Any suggestions to improve this program are welcome! Enjoy 😉


