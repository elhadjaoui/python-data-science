import sys


def main():
    '''Print the number of characters, upper case letters, lower case letters,
    punctuations, spaces and digits in a string
    '''
    try:
        str = ''
        if len(sys.argv) > 2:
            raise AssertionError("more than one argument is provided")
        elif len(sys.argv) < 2:
            try:
                str = input("What is the text to count?\n")
                str += '\n'
            except EOFError:
                pass
        else:
            str = sys.argv[1]
        upper_case_count = sum(1 for char in str if char.isupper())
        lower_case_count = sum(1 for char in str if char.islower())
        punc_char = "!\"#$%&'()*+,-./:;<=>?@[\\]^_`{|}~"
        punctuation_count = sum(1 for char in str if char in punc_char)
        space_count = sum(1 for char in str if char.isspace())
        digit_count = sum(1 for char in str if char.isdigit())
        print(f"the text contains {len(str)} characters:")
        print(f"{upper_case_count} upper letters")
        print(f"{lower_case_count} lower letters")
        print(f"{punctuation_count} punctuations")
        print(f"{space_count} spaces")
        print(f"{digit_count} digits")
    except AssertionError as e:
        print(f"AssertionError: {e}")


if __name__ == "__main__":
    '''Call the main function'''
    main()
