from S1E9 import Character


class Baratheon(Character):
    __doc__ = """Representing the Baratheon family."""

    def __init__(self, first_name: str, is_alive: bool = True) -> None:
        """__init__

        Args:
            first_name (str): name of the Baratheon
            is_alive (bool, optional): Defaults to True.
        """

        super().__init__(first_name, is_alive)
        self.family_name = "Baratheon"
        self.eyes = "brown"
        self.hairs = "dark"

    def die(self) -> None:
        """die

        calls super method of die()
        """

        super().die()

    @classmethod
    def create_baratheon(cls, first_name: str,
                         is_alive: bool = True) -> object:
        """create_baratheon

        Args:
            first_name (str): name of the Baratheon
            is_alive (bool, optional): Defaults to True.
        """

        return cls(first_name, is_alive)

    def __str__(self) -> str:
        """__str__

        Returns:
            str: returns string of unique values to the class
        """
        return f"Vector: ('{self.family_name}', '{self.eyes}', '{self.hairs}')"

    def __repr__(self) -> str:
        """__repr__

        Returns:
            str: returns string of unique values to the class
        """
        return self.__str__()


class Lannister(Character):
    __doc__ = """Representing the Lannister family."""

    def __init__(self, first_name: str, is_alive: bool = True) -> None:
        """__init__

        Args:
            first_name (str): name of the Lannister
            is_alive (bool, optional): Defaults to True.
        """

        super().__init__(first_name, is_alive)
        self.family_name = "Lannister"
        self.eyes = "blue"
        self.hairs = "light"

    def die(self) -> None:
        """die

        calls super method of die()
        """
        super().die()

    @classmethod
    def create_lannister(cls, first_name: str,
                         is_alive: bool = True) -> object:
        """create_lannister

        Args:
            first_name (str): name of the Lannister
            is_alive (bool, optional): Defaults to True.
        """

        return cls(first_name, is_alive)

    def __str__(self) -> str:
        """__str__

        Returns:
            str: returns string of unique values to the class
        """
        return f"Vector: ({self.family_name}, {self.eyes}, {self.hairs})"

    def __repr__(self) -> str:
        """__repr__

        Returns:
            str: returns string of unique values to the class
        """
        return self.__str__()


def main():
    try:
        Robert = Baratheon("Robert")
        print(Robert.__dict__)
        print(Robert.__str__)
        print(Robert.__repr__)
        print(Robert.is_alive)
        Robert.die()
        print(Robert.is_alive)
        print(Robert.__doc__)
        print("---")
        Cersei = Lannister("Cersei")
        print(Cersei.__dict__)
        print(Cersei.__str__)
        print(Cersei.is_alive)
        print("---")
        Jaine = Lannister.create_lannister("Jaine", True)
        print(f"Name : {Jaine.first_name, type(Jaine).__name__},\
            Alive : {Jaine.is_alive}")
    except Exception as e:
        print(f"{type(e).__name__}: {e}")


if __name__ == "__main__":
    main()
