import os
from os.path import join
from data_cleaning import DataCleaning
from caesar_cipher import CaesarCipher
from shift import Shift


class Crack:
    """
    This represents the business logic of the program.
    Inside of Crack class I ask to the user some istructions to
    manage the tasks in order to create, at the end, a file with
    decoded message using DataCleaning, CaesarCipher and Shift classes

    The decoded files will be placed at the decoded-files folder.
    If the Crack Caesar Chiper program can't decrypt the file passed,
    the program quit immediately.

    Input scheme syntax:
    Istruction: start with ">>> " 
    Error message: "ERROR: <error message>"
    Description: "DESCRIPTION: <description message>"
    """

    def __init__(self):
        
        self.files = DataCleaning().get_dict_of_files()
        
        files_in_cases = self.show_files()
        while files_in_cases == False:
            files_in_cases = self.show_files()  # return files in cases folder
        
        id = input("\n>>> Select the ID number of wich file you want to decrypt: ")
        self.fname = self.get_file(id)
        while self.fname == False:
            id = input("\n>>> Select the ID number of wich file you want to decrypt: ")
            self.fname = self.get_file(id)  # return file name chosen from the user

        self.parse_file = DataCleaning(self.fname)  # create a DataCleaning obj to parse the fname passed
        self.most_common_char = self.parse_file.most_common_letter()  # return the most common char finded in parsed file

        """
        Shift().list_of_vowels has the vowels ordered by the most common frequency in texts (start with 'e')
        self.shift_values return a list of int that is the difference between most common letter frequency 
        and most_common_char finded inside file chosen by the user
        """
        self.shift_values = Shift().difference_between_ascii_chars(self.most_common_char)
        self.first_500_lines_message = self.parse_file.read_only_500_lines()  # read only the first 500 lines of possible decrypted message and prompt the output for the user

        shift = self.parse_shift()  # is shift value that CaesarCipher().decrypt() needs to decode the message
        message = CaesarCipher(self.parse_file.read_file(), shift)  # create the entire decrypted message 
        self.decoded_message = message.decrypt()  # return the decrypted message
        create_decoded_file = self.make_file(self.decoded_message)

        self.quit_program("q")
        

    def quit_program(self, istruction):
        if istruction.lower() == "q":
            print("\nQuitting program ...\n")
            quit()
        return False
    

    def show_files(self):
        print("\n" + ":"*20 + " Crack Caesar Chipher " + ":"*20 + "\n")
        istruction = input(">>> Please press enter to see available files in cases folder (press q to quit the program) ")
        # empty string return False, so in this case we need evaluete to True from not istruction and continue the program
        if self.quit_program(istruction) or not istruction:  
            print("\nID\t NAME\n"+"-"*50)
            for key, value in self.files.items():
                print(f"{key}\t {value}")
            return True
        else:
            print(f'\nERROR: "{istruction}" Is not valid input. Press enter or q to quit the program\n')
            return False
    
    
    def get_file(self, file_id):
        if file_id == "q":
                self.quit_program(file_id)
        try:
            id = int(file_id)
            if id in self.files.keys():
                return self.files[id]
            print(f'\nERROR: "{file_id}" Is not valid input. Try Again (press q to quit the program)')
            return False
        except:
            print(f'\nERROR: "{file_id}" Is not valid input. Try Again (press q to quit the program)')
            return False


    def parse_shift(self):
        index = 0
        print("\n" + ":"*62 + "\n")
        print(self.first_500_lines_message, end=" [...]\n")
        print("\n" + ":"*62 + "\n")
        print(f"DESCRIPTION: Those are the first 500 words encrypted from the original version of '{self.fname}' file")
        input("\n>>> Press any key to continue ")
        for shift in range(index, len(self.shift_values)):

            print("\n" + ":"*20 + " Decrypting 500 words " + ":"*20 + "\n")
            print(CaesarCipher(self.first_500_lines_message, self.shift_values[shift]).decrypt(), end=" [...]\n")
            print("\n" + ":"*62 + "\n")
            print(f"ATTEMPT N. {index+1}")
            print(f"DESCRIPTION: Those are the first 500 words decrypted by shifting the the most common char '{self.most_common_char}' (finded in the original version of '{self.fname}' file), with '{Shift().list_of_vowels[index]}'.")
            check = input("\n>>> This version of decryption makes sense in your natural language? (y/n)").lower()
            if check == "y":
                print(f"\nLook at decoded-files folder. I've just created a new file called '{self.fname}' with the decoded message inside ;)")
                return self.shift_values[shift]
    
            index += 1

        print("\nGAME OVER: The possible shift values are finished. The Crack Caesar Cipher program can't decrypt this message. You have to find another way... I'm sorry :(")
        print("\n" + ":"*62 + "\n")
        self.quit_program('q')
        return False


    def make_file(self, decode_file):
        if self.parse_shift:
            with open(self.path_for_decoded_files(), 'w') as decoded_file:
                return decoded_file.write(decode_file)


    def path_for_decoded_files(self):
        current_path = os.getcwd()  # get current working directory
        decoded_files_path = os.path.join(current_path, "decoded-files", self.fname)
        return decoded_files_path
    

# TEST
def main():
    test = Crack()


if __name__ == "__main__":
    main()