from input import InputBot


def main():

    while True:
        input_bot = input("Enter the input (BLANK to quit): ")
        if input_bot.lower() == "":
            print("Bye bye!")
            break

        try:
            prefix, suffix = input_bot.lower().split(" is ")
            robot = InputBot(prefix, suffix)
            print(robot.checkInput())

        except:
            print("I have no idea what you are talking about\n")


if __name__ == "__main__":
    main()
