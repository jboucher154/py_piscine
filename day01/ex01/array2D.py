import numpy as np


def slice_me(family: list, start: int, end: int) -> list:
    """slice_me(2DArray of lists, start index, end index)
--> sliced list

prints shape of passed 2DArray, slices it based on indexes passed.
Returns the sliced array as a list."""

    for entry in family:
        if not isinstance(entry, list):
            raise TypeError("non 'list' element found in 'family'")
    sizes = [len(x) for x in family]
    if sum(sizes) / len(sizes) != sizes[0]:
        raise ValueError("not all nested lists are the same size")
    # make np array for family
    family_arr = np.array(family)
    # print the shape
    print("My shape is :", family_arr.shape)
    # slice it up!
    sliced = np.array(family_arr[start:end])
    # return it
    print("My new shape is :", sliced.shape)
    return sliced.tolist()


def main():
    """main() tests for slice_me
    """
    family = [[1.80, 78.4], [2.15, 102.7], [2.10, 98.5], [1.88, 75.2]]

    print(slice_me(family, 2, -1))


if __name__ == "__main__":
    main()
