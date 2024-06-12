import pandas as pd


def load(path: str) -> pd.DataFrame | None:
    """load

    Args:
        path (str): absolute path to csv file to load

    Returns:
        pd.DataFrame | None: The data loaded into a pandas DataFrame or
        None if an error occurs while loading file.
    """

    try:
        df = pd.read_csv(path)
        print("Loading dataset of dimensions", df.shape)
        return df
    except Exception as e:
        print(f"{type(e).__name__}: {e}")
        return None


def main():
    """main tests for load func"""
    
    try:
        print(load("life_expectancy_years.csv"))
    except Exception as e:
        print(f"{type(e).__name__}: {e}")


if __name__ == "__main__":
    main()
