from load_csv import load
import matplotlib.pyplot as plt
import matplotlib.ticker as ticker
import pandas as pd


def set_x_ticks(tick_val: float, pos: int) -> str:
    """set_x_ticks

    Args:
        tick_val (float): x axis tick value to be formatted
        pos (int): tic position on graph

    Returns:
        str: new tick label
    """

    if tick_val > 999:
        new_label = f"{tick_val / 1000:.0f}k"
    else:
        new_label = str(tick_val)
    return new_label


def display(df: pd.DataFrame) -> None:
    """display

    Args:
        df (pd.DataFrame): take data for life and gdp and displays
        with matplotlib. Adjusts x scale to be logrithmic.
    """

    ax1 = df.plot.scatter(x="gdp_per_capita", y="life_expectancy", c="purple")
    ax1.set_xlim(left=300, right=11000)
    ax1.set_xscale("log")
    tick_locator = ticker.FixedLocator([300, 1000, 10000])
    ax1.xaxis.set_major_locator(tick_locator)
    ax1.xaxis.set_major_formatter(ticker.FuncFormatter(set_x_ticks))
    plt.xlabel("Gross domestic product")
    plt.ylabel("Life Expectancy")
    plt.title("1900")
    plt.show()


def get_life_and_gdp_data_1900() -> pd.DataFrame:
    """get_life_and_gdp_data_1900

    Returns:
        pd.DataFrame: new data set of life expectancy and gdp per
        capita from the files 'life_expectancy_years.csv'
        'income_per_person_gdppercapita_ppp_inflation_adjusted.csv'
        for the year 1900. Any rows with NaN or Null values are dropped.
    """
    # load data
    income_df = \
        load("income_per_person_gdppercapita_ppp_inflation_adjusted.csv")
    life_df = load("life_expectancy_years.csv")
    # get relevant series
    income1900 = income_df.loc[:, '1900']
    life1900 = life_df.loc[:, '1900']
    # join series into new DataFrame
    joined_df = pd.concat([income1900, life1900], axis=1)
    joined_df.columns = ["gdp_per_capita", "life_expectancy"]
    # remove NaN values
    joined_df = joined_df.dropna()

    return joined_df


def main() -> None:
    """main

    calls to get prepared data, then calls to display it.
    Any exceptions thrown will be caught and printed here.
    """
    try:
        data = get_life_and_gdp_data_1900()
        display(data)
    except Exception as e:
        print(f"{type(e).__name__}: {e}")


if __name__ == "__main__":
    main()
