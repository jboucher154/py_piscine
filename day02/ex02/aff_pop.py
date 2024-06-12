from load_csv import load
import matplotlib.pyplot as plt
import matplotlib.ticker as ticker
import pandas as pd


def verify_data(data: pd.DataFrame, country1: str, country2: str):
    """_summary_

    Args:
        data (DataFrame): dataframe loaded from 'load' function
        country1 (string): country to verify presence in data set
        country2 (string): country to verify presence in data set

    Raises:
        ValueError: if data set does not load and is 'None'
        AssertionError: if desired data is missing from the data set
    """

    if data is None:
        raise ValueError("data is 'None', not loaded")
    assert "country" == data.index.name, "country column missing from data"
    assert country1 in data.index, f"'{country1}' not found in data set"
    assert country2 in data.index, f"'{country2}' not found in data set"


def wrangle_data(data: pd.DataFrame) -> pd.DataFrame:
    """wrangle_data

    Args:
        data (pd.DataFrame): data to manipulate

    Returns:
        _type_: pd.DataFrame of manipulated data with slice taken for
        data limits
    """

    for column in data.columns:
        data[column] = data[column].replace(
                                    {'B': 'e+09', 'M': 'e+06', 'k': 'e+03'},
                                    regex=True).astype(float).astype(int)
    data = data.loc[:, "1800":"2050":1]
    return data


def format_y_ticks(tick_val: float, pos: int) -> str:
    """_summary_

    Args:
        tick_val (float): y axis tick value to be formatted
        pos (int): tic position on graph

    Returns:
        str: of new tick label
    """
    new_label = f"{tick_val/1000000:.0f}M"
    return new_label


def main():
    """main

    Loads and displays population projections for two countries.
    """

    country1 = "Finland"
    country2 = "South Korea"
    try:
        data = load("population_total.csv")
        verify_data(data, country1, country2)
        wrangled_data = wrangle_data(data)
        fin_series = wrangled_data.loc[country1]
        sk_series = wrangled_data.loc[country2]
        plt.gca().yaxis.set_major_formatter(
            ticker.FuncFormatter(format_y_ticks))
        fin_series.plot(color="blue")
        sk_series.plot(color="red")
        plt.title(label="Population Projections")
        plt.xlabel("Year")
        plt.ylabel("Population")
        plt.legend([country1, country2])
        plt.show()
    except Exception as e:
        print(f"{type(e).__name__}: {e}")


if __name__ == "__main__":
    main()
