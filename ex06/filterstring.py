import sys


def my_isdigit(char):
    """Check if a character is a digit"""
    if not (char >= "0" and char <= "9"):
        return False
    return True


def my_ischar(char):
    """Check if a character is a letter"""
    if not (char >= "a" and char <= "z") and not (char >= "A" and char <= "Z"):
        return False
    return True


def is_int(str):
    """Check if a string is an integer"""
    for char in str:
        if my_isdigit(char):
            return False
    return True


def is_string(str):
    """Check if a string is a string"""
    for char in str:
        if not my_ischar(char):  # B
            return False
    return True


def main():
    """Print the number of characters, upper case letters, lower case letters,
    punctuations, spaces and digits in a string
    """
    try:
        if len(sys.argv) > 2:
            raise AssertionError("more than one argument is provided")
    except AssertionError as e:
        print(f"AssertionError: {e}")


if __name__ == "__main__":
    main()
