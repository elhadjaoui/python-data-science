
import pandas as pd
import numpy as np


def load(path: str):
    dates = pd.date_range("20130101", periods=6)
    df = pd.DataFrame(np.random.randn(6, 4), index=dates, columns=list("ABCD"))
    print(df.loc[:, ["A", "B"]])


def main():
    dataset = load("data.csv")
    print(dataset)
    print(load.__doc__)


if __name__ == "__main__":
    main()
