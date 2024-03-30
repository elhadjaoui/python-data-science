
import sys

def main():
    if len(sys.argv) > 2:
        print("AssertionError: more than one argument is provided")
        return
    elif len(sys.argv) < 2:
        return
    try:
        number = int(sys.argv[1])
    except ValueError:
        print("AssertionError: argument is not an integer")
        return
    print("I'm Even." if number % 2 == 0 else "I'm Odd.")
if __name__ == "__main__":
    main()
