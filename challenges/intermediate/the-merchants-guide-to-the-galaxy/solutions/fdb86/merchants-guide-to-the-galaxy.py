from input import InputBot


def main():

    while True:
        user_input = input("Enter the input (BLANK to quit): ")
        if user_input.lower() == "":
            print("Bye bye!")
            break

        try:
            prefix, suffix = user_input.lower().split(" is ")
            robot = InputBot(prefix, suffix)
            print(robot.checkInput())

        except:
            print("I have no idea what you are talking about\n")


if __name__ == "__main__":
    main()
