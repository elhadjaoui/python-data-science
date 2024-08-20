def square(x: int | float) -> int | float:
    """Return the square of the input number.

    Args:
        x (int | float)

    Returns:
        int | float
    """
    return x**2


def pow(x: int | float) -> int | float:
    """Return the power of the input number.

    Args:
        x (int | float)

    Returns:
        int | float
    """
    return x**x


def outer(x: int | float, function) -> object:
    """Return a function that will return the result of the input function
        closure works as a class with only one method
    usecase:
        Closures can be used to avoid global values and provide data hiding.
    Args:
        x (int | float)
        function (_type_)

    Returns:
        object
    """
    count = 0
    count = x

    def inner() -> float:
        nonlocal count
        count = function(count)
        return count
    return inner


def main():
    my_counter = outer(3, square)
    print(my_counter())
    print(my_counter())
    print(my_counter())
    print("---")
    another_counter = outer(1.5, pow)
    print(another_counter())
    print(another_counter())
    print(another_counter())


if __name__ == "__main__":
    main()
