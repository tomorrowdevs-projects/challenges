from caesar_cipher.caesar_cipher import CaesarCipher
from caesar_cipher.message_visualizer import MessageVisualizer


def main():
    choice = input("Press 1 to encode the message or -1 to decode the message: ")
    valid_choice = ["1", "-1"]
    while choice not in valid_choice:
        print(f"{choice} is not a valid value. Please try again")
        choice = input("Press 1 to encode the message or -1 to decode the message: ")

    # Read the message and desired shift value from the user
    message = input("Enter the message: ")
    shift = int(input("Enter the shift value: "))

    secret_message = CaesarCipher(message, shift)

    if choice == "1":
        shift = secret_message.encode()
    else:
        shift = secret_message.decode()

    visualizer = MessageVisualizer(message, shift)
    result = visualizer.print_ticket()
    print(result)


if __name__ == "__main__":
    main()
