from S1E7 import Baratheon, Lannister


class King(Baratheon, Lannister):
    """King class derived from Baratheon and Lannister classes"""

    def __init__(self, first_name, is_alive=True, family_name="Baratheon",
                 eyes="brown", hairs="dark"):
        """ initializes the character

        Args:
            first_name (_type_): _description_
            is_alive (bool, optional): _description_. Defaults to True.
            family_name (str, optional): _description_. Defaults to "Baratheon"
            eyes (str, optional): _description_. Defaults to "brown".
            hairs (str, optional): _description_. Defaults to "dark".
        """
        super().__init__(first_name, is_alive, family_name, eyes, hairs)

    def set_eyes(self, eyes):
        """sets the eyes attribute"""
        self.eyes = eyes

    def get_eyes(self):
        """returns the eyes attribute"""
        return self.eyes

    def set_hairs(self, hairs):
        """sets the hairs attribute"""
        self.hairs = hairs

    def get_hairs(self):
        """returns the hairs attribute"""
        return self.hairs


def main():
    # python uses the C3 linearization algorithm to determine
    # the order of inheritance
    # print(King.__mro__)
    Joffrey = King("Joffrey")
    print(Joffrey.__dict__)
    Joffrey.set_eyes("blue")
    Joffrey.set_hairs("light")
    print(Joffrey.get_eyes())
    print(Joffrey.get_hairs())
    print(Joffrey.__dict__)


if __name__ == "__main__":
    main()
