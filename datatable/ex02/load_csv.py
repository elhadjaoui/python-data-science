import pandas as pd


def load(path: str) -> pd.DataFrame:
    """Load a CSV file and return a DataFrame."""
    try:
        if not path.lower().endswith('.csv'):
            raise AssertionError("Error: The file fromat is not .csv")
        df = pd.read_csv(path)
        print(f"Loading dataset of dimensions {df.shape}")
        return df
    except FileNotFoundError:
        print(f"Error: File {path} not found")
        return None
    except AssertionError as e:
        print(e)
        return None


def main():
    df = load("life_expectancy_years.csv")
    print(df)
    # print(load.__doc__)


if __name__ == "__main__":
    main()
