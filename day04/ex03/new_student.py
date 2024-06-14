import random
import string
from dataclasses import dataclass, field


def generate_id() -> str:
    """generate_id

    Returns:
        str: id string
    Uses random generator to create a 15 character id string
    """
    return "".join(random.choices(string.ascii_lowercase, k=15))


@dataclass
class Student:
    __doc__ = """Student dataclass
    Attributes: name, surname, active status, login, and student id"""

    name: str
    surname: str
    active: bool = field(default=True)
    login: str = field(init=False)
    id: str = field(init=False, default_factory=generate_id)

    def __post_init__(self):
        """__post_init__

        Sets student login based on name and surname given.
        """
        if not self.name:
            raise ValueError("Student 'name' cannot be empty")
        if not self.surname:
            raise ValueError("Student 'surname' cannot be empty")
        self.login = self.name[0] + self.surname


def main():
    """main tests for Student dataclass
    """
    student = Student(name="Henrik", surname="Hen")
    print(student.name, student.surname)
    print(student)
    try:
        student = Student(name="Henrietta", surname="Leaf", id="test")
        print(student.name, student.surname)
        print(student)
    except Exception as e:
        print(f"{type(e).__name__}: {e}")
    try:
        student = Student()
    except Exception as e:
        print(f"{type(e).__name__}: {e}")
    try:
        student = Student(name="", surname="Leaf")
    except Exception as e:
        print(f"{type(e).__name__}: {e}")
    try:
        student = Student(name="Summer", surname="")
    except Exception as e:
        print(f"{type(e).__name__}: {e}")


if __name__ == "__main__":
    main()
