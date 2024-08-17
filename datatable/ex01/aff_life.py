
import matplotlib.pyplot as plt
from load_csv import load


def main():
    # Load the dataset
    df = load("life_expectancy_years.csv")
    # iloc is used to select the first row of Morocco using indexers
    morocco_data = df[df['country'] == 'Morocco'].iloc[0, 1:]
    # Convert the index  to integers and the values to floats
    years = morocco_data.index.astype(int)
    # Convert the values to floats
    life_expectancy = morocco_data.values.astype(float)
    # Plot the data
    plt.plot(years, life_expectancy)
    # Add labels and title
    plt.xlabel('Year')
    plt.ylabel('Life Expectancy')
    plt.title('Morocco Life Expectancy')
    # xticks and yticks are used to set the range of the x and y axes
    plt.xticks(range(years.min(), years.max() + 1, 40))
    plt.yticks(
        range(int(life_expectancy.min()), int(life_expectancy.max()) + 1, 10)
    )
    # Show the plot
    plt.show()


if __name__ == "__main__":
    main()
