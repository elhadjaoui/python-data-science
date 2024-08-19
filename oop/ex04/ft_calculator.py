class calculator:
    """A simple calculator class"""

    def dotproduct(V1: list[float], V2: list[float]) -> None:
        """computes the dot product of two vectors"""
        print(f"Dot Product is: {sum([V1[i] * V2[i] for i in range(len(V1))])}")

    def add_vec(V1: list[float], V2: list[float]) -> None:
        """adds two vectors"""
        print([V1[i] + V2[i] for i in range(len(V1))]) 

    def sous_vec(V1: list[float], V2: list[float]) -> None:
        """subtracts two vectors"""
        print([V1[i] - V2[i] for i in range(len(V1))])


def main():
    a = [5, 10, 2]
    b = [2, 4, 3]
    calculator.dotproduct(a, b)
    calculator.add_vec(a, b)
    calculator.sous_vec(a, b)


if __name__ == "__main__":
    main()
