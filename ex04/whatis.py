import argparse
import sys

parser = argparse.ArgumentParser(exit_on_error=False)
parser.add_argument('integers', type = int, nargs = 1)
try:
    args = parser.parse_args(sys.argv[1:])
    if len(args.integers) > 1:
        print("AssertionError: more than one argument is provided")
        sys.exit(1)
    object = args.integers[0]
    if object % 2 == 0:
        print("I'm Even.")
    else:
        print("I'm Odd.")
except (argparse.ArgumentError) as e:
    print(e.__class__.__name__)
    print("AssertionError: argument is not an integer")
