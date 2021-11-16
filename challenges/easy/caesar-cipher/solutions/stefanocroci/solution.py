alpha = 'abcdefghijklmnopqrstuvwxyz'
def encode(phrase, shift):
    new_phrase = ''
    for i in range(len(phrase)):
        if phrase[i].lower() not in alpha:
            new_phrase += phrase[i]
            continue
        # Find the phrase corresponding index in alpha
        index_alpha = alpha.find(phrase[i].lower())
        # Use mod to consider the cases in which (index + shift) is more than lenght of alpha
        new_index = (index_alpha + shift) % len(alpha) 
        # Convert the output in uppercase if input is uppercase
        if phrase[i].isupper():
            new_phrase += alpha[new_index].upper()
        else:
            new_phrase += alpha[new_index]

    return new_phrase

def decode(phrase, shift):
    return encode(phrase, -shift)

while True:
    print('--------------------------------------------------')
    start = int(input('Hello, digit 1 to encode a phrase or digit 2 to decode a phrase: '))
    if start == 1:
        phrase = input('Please insert the phrase to encode it: ')
        shift = int(input('Insert the shift amount: '))
        encoded_phrase = encode(phrase, shift)
        print(encoded_phrase)
    elif start == 2:
        phrase = input('Please insert the phrase to decode it: ')
        shift = int(input('Insert the shift amount used to encode the phrase: '))
        decoded_phrase = decode(phrase, shift)
        print(decoded_phrase)
    else:
        print('ERROR! digit one or two')
    