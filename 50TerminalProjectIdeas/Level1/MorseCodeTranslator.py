print("Morse Code Translator")
print("-" * 30)

# Morse code dictionary
morse_code_dict = {
    'A': '.-', 'B': '-...', 'C': '-.-.', 'D': '-..', 'E': '.', 'F': '..-.',
    'G': '--.', 'H': '....', 'I': '..', 'J': '.---', 'K': '-.-', 'L': '.-..',
    'M': '--', 'N': '-.', 'O': '---', 'P': '.--.', 'Q': '--.-', 'R': '.-.',
    'S': '...', 'T': '-', 'U': '..-', 'V': '...-', 'W': '.--', 'X': '-..-',
    'Y': '-.--', 'Z': '--..',
    '0': '-----', '1': '.----', '2': '..---', '3': '...--', '4': '....-', 
    '5': '.....', '6': '-....', '7': '--...', '8': '---..', '9': '----.',
    ' ': '/'
}

def text_to_morse(text):
    """Convert text to Morse code."""
    morse_code = []
    for char in text.upper():
        if char in morse_code_dict:
            morse_code.append(morse_code_dict[char])
        else:
            morse_code.append('?')  # Unknown character
    return ' '.join(morse_code)

def morse_to_text(morse):
    """Convert Morse code to text."""
    reverse_dict = {v: k for k, v in morse_code_dict.items()}
    text = []
    for code in morse.split(' '):
        if code in reverse_dict:
            text.append(reverse_dict[code])
        else:
            text.append('?')  # Unknown code
    return ''.join(text)

# User input
choice = input("Choose an option:\n1. Text to Morse Code\n2. Morse Code to Text\nEnter 1 or 2: ")
if choice == '1':
    text = input("Enter text to convert to Morse code: ")
    print("Morse Code:", text_to_morse(text))
elif choice == '2':
    morse = input("Enter Morse code to convert to text: ")
    print("Text:", morse_to_text(morse))
else:
    print("Invalid choice.")

