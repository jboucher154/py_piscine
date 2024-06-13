from abc import ABC, abstractmethod


class Character(ABC):
    __doc__ = """Character class

    Inherits from abstract base class."""

    def __init__(self, first_name: str, is_alive: bool = True):
        """__init__

        Args:
            first_name (str): first name of character
            is_alive (bool, optional): Defaults to True."""

        self.first_name = first_name
        self.is_alive = is_alive
        super().__init__()

    @abstractmethod
    def die(self) -> None:
        """die

        Sets is_alive to false."""

        self.is_alive = False


class Stark(Character):
    __doc__ = """Stark class

    Inherits from Character class."""

    def __init__(self, first_name: str, is_alive: bool = True):
        """__init__

        Args:
            first_name (str): _description_
            is_alive (bool, optional): _description_. Defaults to True."""

        super().__init__(first_name, is_alive)

    def die(self) -> None:
        """die

        Calls super method for parent Character class.
        """

        super().die()


def main():
    try:
        Ned = Stark("Ned")
        print(Ned.__dict__)
        print(Ned.is_alive)
        Ned.die()
        print(Ned.is_alive)
        print(Ned.__doc__)
        print(Ned.__init__.__doc__)
        print(Ned.die.__doc__)
        print("---")
        Lyanna = Stark("Lyanna", False)
        print(Lyanna.__dict__)
        # should cause error
        hodor = Character("hodor")
        hodor.die
    except Exception as e:
        print(f"{type(e).__name__}: {e}")


if __name__ == "__main__":
    main()
