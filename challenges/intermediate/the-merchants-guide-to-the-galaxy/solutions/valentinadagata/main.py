from merchant_guide import *


def main():
    error_message = "I have no idea what you are talking about"
    print("Please insert some galactic values [blank line to quit]: \n")
    input_list = []
    input_metals = []

    while True:
        val = input("Insert galactic value: ")
        if val == "":
            break
        input_list.append(val)

    if instructions_values(input_list) == False:
        print(error_message)
        quit()

    print("Please insert some galactic metals [blank line to quit]: \n")
    while True:
        val = input("Insert galactic metals: ")
        if val == "":
            break
        input_metals.append(val)

    if instruction_metals(input_list, input_metals) == False:
        print(error_message)
        quit()

    print("Please ask me to calculate some credits: \n")
    while True:
        values = input("Ask me the questions: ")
        if values == "":
            break

        if check_question(input_list, input_metals, values) == False:
            print(error_message)
            quit()
        else:
            val, words, met, metals = check_question(input_list, input_metals, values)
            result = calculate_result(val, words, met, metals)

            if metals != "":
                print(f"{words}{metals} is {result} Credits")
            else:
                print(f"{words}is {result}")


if __name__ == '__main__':
    main()

"""
glob is I
prok is V
pish is X
tegj is L

glob glob Silver is 34 Credits
glob prok Gold is 57800 Credits
pish pish Iron is 3910 Credits

how much is pish tegj glob glob ?
how many Credits is glob prok Silver ?
how many Credits is glob prok Gold ?
how many Credits is glob prok Iron ?
how much wood could a woodchuck chuck if a woodchuck could chuck wood ?
"""