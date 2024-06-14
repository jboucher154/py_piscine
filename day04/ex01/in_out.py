def square(x: int | float) -> int | float:
    return x**2


def pow(x: int | float) -> int | float:
    return x**x


def outer(x: int | float, function: callable) -> object:
    count = 0

    def inner() -> float:
        nonlocal count
        res = function(x)
        for i in range(count):
            res = function(res)
        count += 1
        return res
    return inner


def main():
    my_counter = outer(3, square)
    print(my_counter())
    print(my_counter())
    print(my_counter())
    print("---")
    another_counter = outer(1.5, pow)
    print(another_counter())
    print(another_counter())
    print(another_counter())


if __name__ == "__main__":
    main()
