import sys


def my_len(iter):
    '''Return the length of a string'''
    count = 0
    for _ in iter:
        count += 1
    return count


def my_isdigit(char):
    '''Check if a character is a digit'''
    if not (char >= '0' and char <= '9'):
        return False
    return True


def my_islower(char):
    '''Check if a character is a lower case letter'''
    if not (char >= 'a' and char <= 'z'):
        return False
    return True


def my_isupper(char):
    '''Check if a character is an upper case letter'''
    if not (char >= 'A' and char <= 'Z'):
        return False
    return True


def space_count(string):
    '''Count the number of spaces in a string'''
    count = 0
    for char in string:
        if char == ' ' or char == '\t' or char == '\r' or char == '\n' or \
                char == '\v' or char == '\f':
            count += 1
    return count


def punctuation_count(string):
    '''Count the number of punctuations in a string'''
    count = 0
    punctiatons = [',', '.', '!', '?', ':', ';', '-', '(', ')', '[', ']', '{',
                   '}', '<', '>', '/', '\\', '|', '@', '#',
                   '$', '%', '^', '&', '*', '_', '+', '=', '~', '`']
    for char in string:
        if char in punctiatons:
            count += 1
    return count


def lower_case_count(string):
    '''Count the number of lower case letters in a string'''
    count = 0
    for char in string:
        if my_islower(char):
            count += 1
    return count


def upper_case_count(string):
    '''Count the number of upper case letters in a string'''
    count = 0
    for char in string:
        if my_isupper(char):
            count += 1
    return count


def digit_count(string):
    '''Count the number of digits in a string'''
    count = 0
    for char in string:
        if my_isdigit(char):
            count += 1
    return count


def main():
    '''Print the number of characters, upper case letters, lower case letters,
    punctuations, spaces and digits in a string
    '''
    try:
        str = ''
        if my_len(sys.argv) > 2:
            raise AssertionError("more than one argument is provided")
        elif my_len(sys.argv) < 2:
            print("Please enter a text:")
            while True:
                try:
                    str = input()
                    str += '\n'
                except EOFError:
                    break
        else:
            str = sys.argv[1]
        print(f"the text contains {my_len(str)} characters:")
        print(f"{upper_case_count(str)} upper letters")
        print(f"{lower_case_count(str)} lower letters")
        print(f"{punctuation_count(str)} punctuations")
        print(f"{space_count(str)} spaces")
        print(f"{digit_count(str)} digits")
    except AssertionError as e:
        print(f"AssertionError: {e}")


if __name__ == "__main__":
    '''Call the main function'''
    main()
