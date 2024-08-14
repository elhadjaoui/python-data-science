
import pandas as pd
import matplotlib.pyplot as plt


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
    dataset = load("life_expectancy_years.csv")
    print(dataset)
    dataset.plot()
    plt.show()
    print(load.__doc__)


if __name__ == "__main__":
    main()
