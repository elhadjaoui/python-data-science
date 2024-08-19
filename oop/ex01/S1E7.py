from S1E9 import Character


class Baratheon(Character):
    """Baratheon class derived from Character class"""
    def __init__(self, first_name, is_alive=True, family_name="Baratheon",
                 eyes="brown", hairs="dark"):
        """initializes the character"""
        super().__init__(first_name, is_alive)
        self.family_name = family_name
        self.eyes = eyes
        self.hairs = hairs

    def die(self):
        """sets is_alive to False"""
        self.is_alive = False

    def __repr__(self) -> str:
        """repr method returns a string representation of the object"""
        return f"Vector: ({self.family_name}', '{self.eyes}', '{self.hairs}')"

    def __str__(self) -> str:
        """ str method returns a string representation of the object"""
        return f"Vector: ({self.family_name}', '{self.eyes}', '{self.hairs}')"


class Lannister(Character):
    """Lannister class derived from Character class"""
    def __init__(self, first_name, is_alive=True, family_name="Lannister",
                 eyes="blue", hairs="light"):
        """initializes the character"""
        super().__init__(first_name, is_alive)
        self.family_name = family_name
        self.eyes = eyes
        self.hairs = hairs

    def die(self):
        """sets is_alive to False"""
        self.is_alive = False

    def __repr__(self) -> str:
        """repr method returns a string representation of the object"""
        return f"Vector: ({self.family_name}', '{self.eyes}', '{self.hairs}')"

    def __str__(self) -> str:
        """ str method returns a string representation of the object"""
        return f"Vector: ({self.family_name}', '{self.eyes}', '{self.hairs}')"

    def create_lannister(first_name, is_alive) -> Character:
        """returns a new Lannister object"""
        return Lannister(first_name, is_alive)


def main():
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
    print(f"Name : {Jaine.first_name, type(Jaine).__name__}, "
          f"Alive : {Jaine.is_alive}")


if __name__ == "__main__":
    main()
