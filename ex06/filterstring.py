import sys
from ft_filter import ft_filter


def main():
    """Returns a list of words that have a length greater
        than a given number"""
    try:
        if len(sys.argv) != 3:
            raise AssertionError("the arguments are bad")
        str = sys.argv[1]
        try:
            number = int(sys.argv[2])
        except ValueError:
            raise AssertionError("the arguments are bad")
        if not isinstance(number, int):
            raise AssertionError("the arguments are bad")
        print((ft_filter(lambda word: len(word) > number, str.split())))
    except AssertionError as e:
        print(f"AssertionError: {e}")


if __name__ == "__main__":
    """Call the main function"""
    main()
