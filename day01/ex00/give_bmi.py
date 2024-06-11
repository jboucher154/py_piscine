import numpy as np


def give_bmi(height: list[int | float], weight: list[int | float])\
     -> list[int | float]:
    """give_bmi(heights, weights), take 2 lists of integers or floats
in input and returns a list of BMI values."""

    # type error if lists are wrong
    if not all(isinstance(e, (int, float)) for e in height):
        raise TypeError("'height' list contains non 'int' or 'float' types")
    if not all(isinstance(e, (int, float)) for e in weight):
        raise TypeError("'weight' list contains non 'int' or 'float' types")
    # Value error for mismatched lens
    if len(height) != len(weight):
        raise ValueError("lists are not the same length")

    height_arr = np.array(height)
    weight_arr = np.array(weight)
    height_squared = np.square(height_arr)
    bmi = weight_arr / height_squared
    return bmi.tolist()


def apply_limit(bmi: list[int | float], limit: int) -> list[bool]:
    """apply_limit(bmi, limit), accepts a list of integers or floats and an
integer representing a limit as parameters. It returns a list of booleans
(True if above the limit)."""

    if not all(isinstance(e, (int, float)) for e in bmi):
        raise TypeError("'bmi' list contains non 'int' or 'float' types")

    limit_list = [True if x > limit else False for x in bmi]
    return limit_list


def main():
    """main() tests for give_bmi and apply limit
    """
    test_h = [1, 2, 1.2]
    test_w = [2, 3, 4]
    bmis = give_bmi(test_h, test_w)
    apply_limit(bmis, 1)


if __name__ == "__main__":
    main()
