import sys
from ft_filter import ft_filter


def my_isdigit(char):
    """Check if a character is a digit"""
    if not (char >= "0" and char <= "9"):
        return False
    return True


def my_len(string):
    """Return the length of a string"""
    count = 0
    for _ in string:
        count += 1
    return count


def my_ischar(char):
    """Check if a character is a letter"""
    if (
        not (char >= "a" and char <= "z")
        and not (char >= "A" and char <= "Z")
        and not char == " "
    ):
        return False
    return True


def is_int(str):
    """Check if a string is an integer"""
    for char in str:
        if not my_isdigit(char):
            return False
    return True


def is_string(str):
    """Check if a string is a string"""
    for char in str:
        if not my_ischar(char):  # B
            return False
    return True


def split_string_by_space(string):
    """Split a string by space"""
    words = []
    word = ""
    for char in string:
        if char == " ":
            words.append(word)
            word = ""
        else:
            word += char
    words.append(word)
    return words


def get_ascii_for_number(char):
    """Get the ASCII number for a character"""
    ascci_number = {
        "0": 48,
        "1": 49,
        "2": 50,
        "3": 51,
        "4": 52,
        "5": 53,
        "6": 54,
        "7": 55,
        "8": 56,
        "9": 57,
    }
    return ascci_number[char]


def string_2_int(string):
    """Convert a string to an integer"""
    number = 0
    is_negative = False
    if string[0] == "+":
        string = string[1:]
    elif string[0] == "-":
        string = string[1:]
        is_negative = True
    for char in string:
        number = number * 10 + (get_ascii_for_number(char) - 48)
    return number if not is_negative else -number


def main():
    """Print the words in a string that have a length greater
        than a given number"""
    try:
        if my_len(sys.argv) != 3:
            raise AssertionError("the arguments are bad")
        str = sys.argv[1]
        number = sys.argv[2]
        if not is_int(number):
            raise AssertionError("the arguments are bad")
        len = string_2_int(number)
        words = split_string_by_space(str)
        print((ft_filter(lambda word: my_len(word) > len, words)))
    except AssertionError as e:
        print(f"AssertionError: {e}")


if __name__ == "__main__":
    """Call the main function"""
    main()
