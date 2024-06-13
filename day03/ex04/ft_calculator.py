class calculator:
    __doc__ = """a humble calculator"""

    @staticmethod
    def dotproduct(V1: list[float], V2: list[float]) -> None:
        products = [i1 * i2 for i1, i2 in zip(V1, V2)]
        summed = sum(products)
        print(f"Dot product is: {summed}")

    @staticmethod
    def add_vec(V1: list[float], V2: list[float]) -> None:
        added = [float(i1) + float(i2) for i1, i2 in zip(V1, V2)]
        print(f"Add Vector is: {added}")

    @staticmethod
    def sous_vec(V1: list[float], V2: list[float]) -> None:
        subtracted = [float(i1) - float(i2) for i1, i2 in zip(V1, V2)]
        print(f"Sous Vector is: {subtracted}")


def main():
    a = [5, 10, 2]
    b = [2, 4, 3]
    calculator.dotproduct(a, b)
    calculator.add_vec(a, b)
    calculator.sous_vec(a, b)


if __name__ == "__main__":
    main()
