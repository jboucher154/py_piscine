from load_csv import load
import matplotlib.pyplot as plt


def main():
    """main

    Raises:
        ValueError: if data set does not load and is 'None'
        AssertionError: if desired data is missing from the data set

    Loads "life_expectancy_years.csv" and plots the data for Finland
    """
    country = "Finland"
    try:
        data = load("life_expectancy_years.csv")
        if data is None:
            raise ValueError("Data not loaded")
        assert "country" == data.index.name, "country column missing from data"
        assert country in data.index, f"'{country}' not found in data set"
        country_series = data.loc[country]
        country_series.plot(color="green")
        plt.title(label=f"{country} Life Expectancy Projections")
        plt.xlabel("Life Expectancy")
        plt.ylabel("Year")
        plt.show()
    except Exception as e:
        print(f"{type(e).__name__}: {e}")


if __name__ == "__main__":
    main()
