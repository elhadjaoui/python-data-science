
import pandas as pd


def load(path: str):
    """Load a CSV file and return a DataFrame."""
    try:
        data = pd.read_csv(path)
        return data
    except FileNotFoundError:
        print(f"File {path} not found")
        return None


def main():
    dataset = load("population_total.csv")
    print(dataset)
    print(load.__doc__)


if __name__ == "__main__":
    main()
