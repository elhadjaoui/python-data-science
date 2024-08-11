import numpy as np


def give_bmi(
    height: list[int | float],
    weight: list[int | float]
) -> list[int | float]:
    """Return a list of BMI values.
    args:
        height: list[int | float] - list of height values
        weight: list[int | float] - list of weight values
    returns:
        list[int | float] - list of BMI values
    """
    try:
        if len(height) != len(weight):
            raise ValueError("height and weight must have the same length")
        height_np = np.array(height)
        weight_np = np.array(weight)
        if height_np.dtype != float and height_np.dtype != int:
            raise ValueError("height must be a list of int or float")
        if weight_np.dtype != float and weight_np.dtype != int:
            raise ValueError("weight must be a list of int or float")
        # The any() function returns True if any item in an iterable are true,
        # otherwise it returns False.
        if (height_np <= 0).any():
            raise ValueError("height must be greater than 0")
        if (weight_np <= 0).any():
            raise ValueError("weight must be greater than 0")
        bmi = weight_np / (height_np ** 2)
        return bmi.tolist()
    except ValueError as e:
        print(e)
        exit(1)


def apply_limit(bmi: list[int | float], limit: int) -> list[bool]:
    """Return a list of booleans indicating if the BMI is greater
    than the limit.
    args:
        bmi: list[int | float] - list of BMI values
        limit: int - limit value
    returns:
        list[bool] - list of booleans indicating if the BMI is greater
        than the limit
    """
    try:
        if not isinstance(limit, float) and not isinstance(limit, int):
            raise ValueError("limit must be an integer")
        if limit <= 0:
            raise ValueError("limit must be greater than 0")
        bmi_np = np.array(bmi)
        if bmi_np.dtype != float and bmi_np.dtype != int:
            raise ValueError("bmi must be a list of int or float")
        if (bmi_np <= 0).any():
            raise ValueError("bmi must be greater than 0")
        return (bmi_np > limit).tolist()
    except ValueError as e:
        print(e)
        exit(1)


def main():
    height = [2.71, 1.15]
    weight = [165.3, 38.4]
    bmi = give_bmi(height, weight)
    print(give_bmi.__doc__)
    print(bmi, type(bmi))
    print(apply_limit(bmi, 26))


if __name__ == "__main__":
    main()
