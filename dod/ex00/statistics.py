

def get_mean(data: list) -> float:
    """returns the mean of a list of numbers"""
    return sum(data) / len(data)


def get_std(data: list) -> float:
    """returns the standard deviation of a list of numbers"""
    mean = get_mean(data)
    return (sum([(x - mean) ** 2 for x in data]) / len(data)) ** 0.5


def get_variance(data: list) -> float:
    """returns the variance of a list of numbers"""
    mean = get_mean(data)
    return sum([(x - mean) ** 2 for x in data]) / len(data)


def get_median(data: list) -> float:
    """returns the median of a list of numbers"""
    n = len(data)
    return (data[n // 2] if n % 2 != 0
            else (data[n // 2 - 1] + data[n // 2]) / 2)


def get_quartile(data: list) -> list:
    """returns the quartile of a list of numbers"""
    n = len(data)
    q1 = (data[n // 4] if n % 4 != 0
          else (data[n // 4 - 1] + data[n // 4]) / 2)
    q3 = (data[3 * n // 4] if n % 4 != 0
          else (data[3 * n // 4 - 1] + data[3 * n // 4]) / 2)
    return [q1/1, q3/1]  # return as list of floats


def ft_statistics(*args: any, **kwargs: any) -> None:
    """computes the sum, mean, median, variance
    and standard deviation of a list of numbers"""
    m = ["mean", "std", "var", "median", "quartile"]
    data = list(args)
    func = list(kwargs.values())
    if not all(isinstance(x, int) for x in data):
        print("Error")
        return
    if not all(x in m for x in func) or len(kwargs) == 0:
        return
    data.sort()

    for key, value in kwargs.items():
        try:
            assert len(data) > 0, "Error"
            if value == "mean":
                print(f"Mean : {get_mean(data)}")
            elif value == "std":
                print(f"std : {get_std(data)}")
            elif value == "var":
                print(f"var : {get_variance(data)}")
            elif value == "median":
                print(f"median : {get_median(data)}")
            elif value == "quartile":
                print(f"Quartile: {get_quartile(data)}")
            else:
                print("Error")
                return
        except AssertionError as e:
            print(e)


def main():
    ft_statistics(1, 42, 360, 11, 64, toto="mean", tutu="median",
                  tata="quartile")
    print("-----")
    ft_statistics(5, 75, 450, 18, 597, 27474, 48575, hello="std", world="var")
    print("-----")
    ft_statistics(5, 75, 450, 18, 597, 27474, 48575, ejfhhe="heheh",
                  ejdjdejn="kdekem")
    print("-----")
    ft_statistics(toto="mean", tutu="median", tata="quartile")


if __name__ == "__main__":
    main()
