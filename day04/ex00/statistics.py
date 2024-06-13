def calc_mean(args: tuple[int | float]) -> float | None:
    """calc_mean

    Args:
        args (tuple[int | float]): args passed to ft_statistics,
        should be numeric

    Returns:
        float | None: calculated mean or None if error
    """
    if len(args) == 0 or not all(isinstance(x, (int, float)) for x in args):
        return None
    else:
        mean = sum(args) / len(args)
        return mean


def find_median(args: tuple[int | float]) -> float | None:
    """find_median

    Args:
        args (tuple[int  |  float]): args passed to ft_statistics,
        should be numeric

    Returns:
        float | None: median of args passed or None if error
    """
    if len(args) == 0 or not all(isinstance(x, (int, float)) for x in args):
        return None
    else:
        arg_list = list(args)
        arg_list.sort()
        mid_index = len(args) // 2
        median = arg_list[mid_index]
        return median


def find_quartiles(args: tuple[int | float]) -> list[float] | None:
    """find_quartiles

    Args:
        args (tuple[int  |  float]): args passed to ft_statistics,
        should be numeric

    Returns:
        list[float] | None: list of 25th and 75th quartiles or None if error
    """
    if len(args) == 0 or not all(isinstance(x, (int, float)) for x in args):
        return None
    else:
        qrtls = []
        arg_list = list(args)
        arg_list.sort()
        length = len(args)
        # len of 0, 1, 2?
        mid_index = length // 2
        first_quartile = float(arg_list[(length - mid_index) // 2])
        third_quartile = float(arg_list[mid_index + mid_index // 2])
        qrtls.append(first_quartile)
        qrtls.append(third_quartile)
        return qrtls


def get_standard_deviation(args: tuple[int | float]) -> float | None:
    """get_standard_deviation

    Args:
        args (tuple[int  |  float]): args passed to ft_statistics,
        should be numeric

    Returns:
        float | None: standard deviation of args or None if error
    """
    if len(args) == 0 or not all(isinstance(x, (int, float)) for x in args):
        return None
    else:
        mean = calc_mean(args)
        mean_diffs = [(x - mean)**2 for x in args]
        sum_of_mean_diffs = sum(mean_diffs)
        divided = sum_of_mean_diffs / len(args)
        std_div = divided**(1/2)
        return std_div


def get_variance(args: tuple[int | float]) -> float | None:
    """get_variance

    Args:
        args (tuple[int  |  float]): args passed to ft_statistics,
        should be numeric

    Returns:
        float | None: calculated variance of args population or
        None if error
    """
    if len(args) == 0 or not all(isinstance(x, (int, float)) for x in args):
        return None
    else:
        mean = calc_mean(args)
        mean_diffs = [(x - mean)**2 for x in args]
        sum_of_mean_diffs = sum(mean_diffs)
        variance = sum_of_mean_diffs / len(args)
        return variance


def ft_statistics(*args: any, **kwargs: any) -> None:
    """ft_statistics

    Args:
        *args (any): data to be processed
        **kwargs (any): values indicate calculations to be done.
        Valid values: [mean, median, std, quartile, var]
    """
    stats_dict = {
        "mean": calc_mean,
        "median": find_median,
        "std": get_standard_deviation,
        "quartile": find_quartiles,
        "var": get_variance
    }

    for key, value in kwargs.items():
        if value in stats_dict:
            res = stats_dict[value](args)
            if not res:
                print("ERROR")
            else:
                print(f"{value} : {res}")


def main():
    ft_statistics(1, 42, 360, 11, 64, toto="mean", tutu="median",
                  tata="quartile")
    print("-----")
    ft_statistics(5, 75, 450, 18, 597, 27474, 48575, hello="std",
                  world="var")
    print("-----")
    ft_statistics(5, 75, 450, 18, 597, 27474, 48575, ejfhhe="heheh",
                  ejdjdejn="kdekem")
    print("-----")
    ft_statistics(toto="mean", tutu="median", tata="quartile")


if __name__ == "__main__":
    main()
