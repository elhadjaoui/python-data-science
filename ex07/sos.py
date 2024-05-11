import sys


def my_len(string):
    """Return the length of the string given in argument"""
    count = 0
    for _ in string:
        count += 1
    return count


def main():
    """Print the morse code of the string given in argument"""
    UPPERCASE_MAPPING = {
        "a": "A",
        "b": "B",
        "c": "C",
        "d": "D",
        "e": "E",
        "f": "F",
        "g": "G",
        "h": "H",
        "i": "I",
        "j": "J",
        "k": "K",
        "l": "L",
        "m": "M",
        "n": "N",
        "o": "O",
        "p": "P",
        "q": "Q",
        "r": "R",
        "s": "S",
        "t": "T",
        "u": "U",
        "v": "V",
        "w": "W",
        "x": "X",
        "y": "Y",
        "z": "Z",
    }
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
        if my_len(sys.argv) != 2:
            raise AssertionError()
        str = sys.argv[1]
        for char in str:
            if UPPERCASE_MAPPING[char] not in NESTED_MORSE:
                raise KeyError()
            else:
                res += NESTED_MORSE[UPPERCASE_MAPPING[char]] + " "
        print(res[:-1])
    except (AssertionError, KeyError):
        print("AssertionError: The arguments are bad")


if __name__ == "__main__":
    """Call the main function"""
    main()
