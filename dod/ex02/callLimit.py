def callLimit(limit: int):
    """Decorator to limit the number of calls to a function.

    Args:
        limit (int): Maximum number of allowed calls.

    Returns:
        function: A decorator that enforces the call limit.
    """
    try:
        limit = int(limit)
        if limit <= 0:
            raise ValueError("Limit must be greater than 0")
    except ValueError as e:
        print(f"Invalid limit: {e}")
        return None

    def callLimiter(function):
        """Wrapper function that enforces the call limit."""
        count = 0

        def limit_function(*args, **kwargs):
            nonlocal count
            try:
                if count >= limit:
                    msg = f"Error: {function} call too many times"
                    raise RuntimeError(msg)
                count += 1
                return function(*args, **kwargs)
            except RuntimeError as e:
                print(e)
                return None
        return limit_function

    return callLimiter


def main():
    @callLimit(-1)
    def f():
        print("f()")

    @callLimit(1)
    def g():
        print("g()")

    for _ in range(3):
        try:
            f()
        except RuntimeError as e:
            print(e)

        try:
            g()
        except RuntimeError as e:
            print(e)


if __name__ == "__main__":
    main()
