import sys


def main():
    """Print the morse code of the string given in argument"""
    NESTED_MORSE = {
        "A": ".-",
        "B": "-...",
        "C": "-.-.",
        "D": "-..",
        "E": ".",
        "F": "..-.",
        "G": "--.",
        "H": "....",
        "I": "..",
        "J": ".---",
        "K": "-.-",
        "L": ".-..",
        "M": "--",
        "N": "-.",
        "O": "---",
        "P": ".--.",
        "Q": "--.-",
        "R": ".-.",
        "S": "...",
        "T": "-",
        "U": "..-",
        "V": "...-",
        "W": ".--",
        "X": "-..-",
        "Y": "-.--",
        "Z": "--..",
        "0": "-----",
        "1": ".----",
        "2": "..---",
        "3": "...--",
        "4": "....-",
        "5": ".....",
        "6": "-....",
        "7": "--...",
        "8": "---..",
        "9": "----.",
        " ": "/",
    }
    res = ""
    try:
        if len(sys.argv) != 2:
            raise AssertionError()
        str = sys.argv[1]
        for char in str:
            if char.upper() not in NESTED_MORSE:
                raise KeyError()
            else:
                res += NESTED_MORSE[char.upper()] + " "
        print(res[:-1])
    except (AssertionError, KeyError):
        print("AssertionError: The arguments are bad")


if __name__ == "__main__":
    """Call the main function"""
    main()
