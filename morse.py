
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

    morse_message = message.split(" / ")
    converted_message = []

    print(f'Morse message : {morse_message}')

    for morse_word in morse_message:
        print(f'Converting morse word {morse_word} into letters...')
        converted_message.append(decode_word(morse_word))

    print(f'==> Converted message : {converted_message}')
    return " ".join(converted_message)

def decode_word(word):
    morse_word = word.split(" ")
    converted_word = ""

    print(f' -> Morse word : {morse_word}')

    for symbol in morse_word:
        print(f' -> Converting symbol {symbol} into letter {ALPHABET[symbol]}')
        converted_word += ALPHABET[symbol]

    print(f' => Converted word : {converted_word}')
    return converted_word


if __name__ == "__main__":
    print(decode("... --- ..."))
    print(decode("-..-"))
    print(decode(".- .-.. .-.. / -.-- --- ..- / -. . . -.. / .. ... / -.-. --- -.. ."))
