letter_to_morse = {
    'a':'.-', 'b':'-...', 'c':'-.-.', 'd':'-..', 'e':'.', 'f':'..-.', 
    'g':'--.', 'h':'....', 'i':'..', 'j':'.---', 'k':'-.-', 'l':'.-..', 'm':'--', 
    'n':'-.', 'o':'---', 'p':'.--.', 'q':'--.-', 'r':'.-.', 's':'...', 't':'-',
    'u':'..-', 'v':'...-', 'w':'.--', 'x':'-..-', 'y':'-.--', 'z':'--..',
    '0':'-----', '1':'.----', '2':'..---', '3':'...--', '4':'....-',
    '5':'.....', '6':'-....', '7':'--...', '8':'---..', '9':'----.', ' ':'/'
}

# We need to invert the dictionary. This will create a dictionary
# that can go from the morse back to the letter
morse_to_letter = {}
for letter in letter_to_morse:
    morse = letter_to_morse[letter]
    morse_to_letter[morse] = letter

def encode(message):
    if "!" in message:
        raise ValueError(f"'!' is not valid in English strings")

    morse = [letter_to_morse[letter] for letter in message.lower()]

    morse_message = " ".join(morse)
    
    return morse_message
    
def decode(message):
    english = [morse_to_letter[letter] for letter in message.split(" ")]

    english_message = "".join(english)
    
    return english_message