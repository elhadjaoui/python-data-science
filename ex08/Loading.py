
import time
import sys


def main():
    """ simulate the loading like tqdm """

    for i in range(100):
        time.sleep(0.1)
        sys.stdout.write("\r[%-100s] %d%%" % ('=' * i, i))
        sys.stdout.flush()
    print()


if __name__ == "__main__":
    """Run the main function"""
    main()