import numpy as np


def slice_me(family: list, start: int, end: int) -> list:
    """Return a slice of a 2D array.

    args:
        family: list - list of lists
        start: int - start index
        end: int - end index
    returns:
        list - slice of the 2D array
    """
    try:
        if not isinstance(family, list):
            raise ValueError("family must be a list ")
        if not isinstance(start, int) or not isinstance(end, int):
            raise ValueError("start and end must be integers")
        if not all(len(item) == len(family[0]) for item in family):
            raise ValueError("lists with different sizes.")
        arr = np.array(family)
        print(f"My shape is : {arr.shape}")
        new_arr = arr[start:end]
        print(f"My new shape is : {new_arr.shape}")
        return new_arr.tolist()
    except ValueError as e:
        print(e)
        exit(1)


def main():
    family = [[1.80, 78.4], [2.15, 102.7], [2.10, 98.5], [1.88, 75.2]]
    print(slice_me(family, 0, 2))
    print(slice_me(family, 1, -2))


if __name__ == "__main__":
    main()
