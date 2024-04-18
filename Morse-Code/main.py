run = True

# Morse conversion for standard alphabet
morse_code_dictionary = {
    'a': '.-',
    'b': '-...',
    'c': '-.-.',
    'd': '-..',
    'e': '.',
    'f': '..-.',
    'g': '--.',
    'h': '....',
    'i': '..',
    'j': '.---',
    'k': '-.-',
    'l': '.-..',
    'm': '--',
    'n': '-.',
    'o': '---',
    'p': '.--.',
    'q': '--.-',
    'r': '.-.',
    's': '...',
    't': '-',
    'u': '..-',
    'v': '...-',
    'w': '.--',
    'x': '-..-',
    'y': '-.--',
    'z': '--..',
    ' ': '/',
    ' / ': ' ',
}

# Main script

while run:
    morse = ''
    morse_dic = []
    choice = input("Would you like to encode or decode a message?\n")

    # Text to morse code

    if choice == 'encode':
        text = input("Please enter text to encode to morse: ")
        for letter in text:
            new_letter = morse_code_dictionary[letter]
            morse += new_letter + ' '
        print(f"Your encoded message: {morse}")

    # Morse Code to text

    elif choice == 'decode':
        text = input("Please enter text you would like to decode: ")
        new_text = text.split(" ")

    #  Get each alphabet dictionary key by using the code values

        for value in new_text:
            morse_dic += [key for key, val in morse_code_dictionary.items() if val == value]

        # Join dictionary keys to form decoded string

        for key in morse_dic:
            morse += morse_code_dictionary.get('', key)
        print(f"Your decoded message: {morse}")
    else:
        print("Check your spelling and try again.")
