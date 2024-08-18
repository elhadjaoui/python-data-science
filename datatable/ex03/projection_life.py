
import matplotlib.pyplot as plt  # type: ignore
from load_csv import load


def main():
    """Load the life expectancy and GDP datasets and plot the data."""
    # Load the dataset
    df = load("life_expectancy_years.csv")
    df2 = load("income_per_person_gdppercapita_ppp_inflation_adjusted.csv")
    if df is None or df2 is None:
        return
    data = df['1900']
    data2 = df2['1900']
    # nan values are replaced with the average of the previous and next values
    data = data.interpolate()
    # print(data.values.astype(float))
    life_expectancy = data.values.astype(int)
    gdp = data2.values.astype(int)
    # Plot the data
    plt.scatter(gdp, life_expectancy)
    plt.xscale('log')
    # Add labels and title
    plt.xlabel('Gross Domestic Product')
    plt.ylabel('Life Expectancy')
    plt.title('1900')
    # xticks and yticks are used to set the range of the x and y axes
    plt.xticks([300, 1000, 10000], ['300', '1k', '10k'])
    plt.yticks(range(20, 60, 5))
    # Show the plot
    plt.show()


if __name__ == "__main__":
    main()
