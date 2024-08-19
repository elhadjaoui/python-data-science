from abc import ABC, abstractmethod


class Character(ABC):
    """base class/abstract class"""
    def __init__(self, first_name, is_alive=True):
        """initializes the character"""
        self.first_name = first_name
        self.is_alive = is_alive

    @abstractmethod
    def die(self):
        """abstract method"""
        pass


class Stark(Character):
    """derived class"""

    def __init__(self, first_name, is_alive=True):
        """initializes the character"""
        super().__init__(first_name, is_alive)

    def die(self):
        """sets is_alive to False"""
        self.is_alive = False


def main():
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


if __name__ == "__main__":
    main()
