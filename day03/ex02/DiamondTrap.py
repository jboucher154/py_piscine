from S1E7 import Baratheon, Lannister


class King(Baratheon, Lannister):
    __doc__ = """King of someplace"""

    def __init__(self, first_name: str, is_alive: bool = True) -> None:
        """__init__

        Args:
            first_name (str): name of the King
            is_alive (bool, optional): Defaults to True.
        """
        super().__init__(first_name, is_alive)

    def set_eyes(self, eye_color: str) -> None:
        """set_eyes

        Args:
            eye_color (str): new eye color
        """

        self.eyes = eye_color

    def set_hairs(self, hair_color: str) -> None:
        """set_hairs

        Args:
            hair_color (str): new hair color
        """

        self.hairs = hair_color

    def get_eyes(self) -> str:
        """get_eyes

        Returns:
            str: eye color
        """
        return self.eyes

    def get_hairs(self) -> str:
        """get_hairs

        Returns:
            str: hair color
        """
        return self.hairs

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

    property(get_eyes, set_eyes)
    property(get_hairs, set_hairs)


def main():
    Joffrey = King("Joffrey")
    print(Joffrey.__dict__)
    Joffrey.set_eyes("blue")
    Joffrey.set_hairs("light")
    print(Joffrey.get_eyes())
    print(Joffrey.get_hairs())
    print(Joffrey.__dict__)


if __name__ == "__main__":
    main()
