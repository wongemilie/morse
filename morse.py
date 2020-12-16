
# morse.py
# pylint: disable=missing-docstring

ALPHABET = {
    '.-':   'A',
    '-...': 'B',
    '-.-.': 'C',
    '-..':  'D',
    '.':    'E',
    '..-.': 'F',
    '--.':  'G',
    '....': 'H',
    '..':   'I',
    '.---': 'J',
    '-.-':  'K',
    '.-..': 'L',
    '--':   'M',
    '-.':   'N',
    '---':  'O',
    '.--.': 'P',
    '--.-': 'Q',
    '.-.':  'R',
    '...':  'S',
    '-':    'T',
    '..-':  'U',
    '...-': 'V',
    '.--':  'W',
    '-..-': 'X',
    '-.--': 'Y',
    '--..': 'Z'
}

def decode(message):
    if not message:
        return ""

    morse_message = message.split(" ")
    converted_message = ""

    print(f'Morse message : {morse_message}')

    for symbol in morse_message:
        print(f'Converting {symbol} into letter...')
        converted_message += ALPHABET[symbol]

    print(f'Converted message : {converted_message}')
    return converted_message #''.join(converted_message)

if __name__ == "__main__":
    print(decode("... --- ..."))
    print(decode("-..-"))
