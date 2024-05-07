import sys


def my_len(string):
    count = 0
    for _ in string:
        count += 1
    return count


def my_isdigit(string):
    for char in string:
        if not (char >= '0' and char <= '9'):
            return False
    return True


def get_ascii_for_number(char):
    ascci_number = {
        '0': 48,
        '1': 49,
        '2': 50,
        '3': 51,
        '4': 52,
        '5': 53,
        '6': 54,
        '7': 55,
        '8': 56,
        '9': 57
     }
    return ascci_number[char]


def my_int(string):
    number = 0
    is_negative = False
    if string[0] == '+':
        string = string[1:]
    elif string[0] == '-':
        string = string[1:]
        is_negative = True
    if not my_isdigit(string):
        print("AssertionError: argument is not an integer")
        return None
    for char in string:
        number = number * 10 + (get_ascii_for_number(char) - 48)
    return number if not is_negative else -number


def main():
    if my_len(sys.argv) > 2:
        print("AssertionError: more than one argument is provided")
        return
    elif my_len(sys.argv) < 2:
        print()
        return
    number = my_int(sys.argv[1])
    if number is None:
        return
    print("I'm Even." if number % 2 == 0 else "I'm Odd.")
    print()


if __name__ == "__main__":
    main()
