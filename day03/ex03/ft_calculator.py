class calculator:
    __doc__ = """calculator"""

    def __init__(self, vector: list) -> None:
        """__init__

        Args:
            vector (list): vector of numeric arguments to
            perform operations with
        """
        self.__vector = vector

    def __add__(self, object) -> None:
        """__add__

        Args:
            object (numeric): to perform operation with
        adds value of object to each item in stored vector
        """
        self.__vector = [val + object for val in self.__vector]
        print(self.__vector)

    def __mul__(self, object) -> None:
        """__mul__

        Args:
            object (numeric): to perform operation with
        each item in stored vector multiplied by value of object
        """
        self.__vector = [val * object for val in self.__vector]
        print(self.__vector)

    def __sub__(self, object) -> None:
        """__sub__

        Args:
            object (numeric): to perform operation with
        subtracts value of object from each item in stored vector
        """
        self.__vector = [val - object for val in self.__vector]
        print(self.__vector)

    def __truediv__(self, object) -> None:
        """__truediv__

        Args:
            object (numeric): to perform operation with
        each item in stored vector divided by value of object
        """
        if object == 0:
            print("Do not divide by zero!")
        else:
            self.__vector = [val / object for val in self.__vector]
            print(self.__vector)


def main():
    v1 = calculator([0.0, 1.0, 2.0, 3.0, 4.0, 5.0])
    v1 + 5
    print("---")
    v2 = calculator([0.0, 1.0, 2.0, 3.0, 4.0, 5.0])
    v2 * 5
    print("---")
    v3 = calculator([10.0, 15.0, 20.0])
    v3 - 5
    v3 / 5


if __name__ == "__main__":
    main()
