import pandas as pd


def load(path: str) -> pd.DataFrame:
    """Load a CSV file and return a DataFrame."""
    try:
        if not path.lower().endswith('.csv'):
            raise AssertionError("Error: The file fromat is not .csv")
        df = pd.read_csv(path, index_col=0)
        print(f"Loading dataset of dimensions {df.shape}")
        return df
    except FileNotFoundError:
        print(f"Error: File {path} not found")
        return None
    except AssertionError as e:
        print(e)
        return None


def main():
    dataset = load("population_total.csv")
    print(dataset)
    print(load.__doc__)


if __name__ == "__main__":
    main()
