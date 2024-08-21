import random
import string
from dataclasses import dataclass, field


def generate_id() -> str:
    """Generate a random id

    Returns:
        str: A random id
    """
    return "".join(random.choices(string.ascii_lowercase, k=15))


@dataclass
class Student:
    """Student class
    """
    name: str
    surname: str
    active: bool = True
    login: str = field(init=False)
    id: str = field(default_factory=generate_id, init=False)

    def __post_init__(self):
        self.login = self.name[0] + self.surname.lower()


def main():
    """Main function
    """
    student = Student(name="Edward", surname="agle")
    print(student)

    student = Student(name="Edward", surname="agle", id="toto")
    print(student)


if __name__ == "__main__":
    main()
