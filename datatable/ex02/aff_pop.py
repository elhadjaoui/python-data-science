
import matplotlib.pyplot as plt
from load_csv import load


def main():
    # Load the dataset
    df = load("population_total.csv")
    if df is None:
        return
    # iloc is used to select the first row of Morocco using indexers
    morocco_data = df[df['country'] == 'Morocco'].iloc[0, 1:]
    france_data = df[df['country'] == 'France'].iloc[0, 1:]
    # Convert the index  to integers and the values to floats
    morocco_years = morocco_data.index.astype(int)
    # Convert the values to floats
    morocco_population = [
        float(x.replace("M", "").replace("K", ""))
        for x in morocco_data.values
    ]
    france_years = france_data.index.astype(int)
    france_population = [
        float(x.replace("M", "").replace("K", ""))
        for x in france_data.values
    ]
    # Plot the data
    plt.plot(morocco_years, morocco_population, label='Morocco')
    plt.plot(france_years, france_population, label='France')
    # Add labels and title
    plt.xlabel('Year')
    plt.ylabel('Population')
    plt.title('Population Projections')
    # xticks and yticks are used to set the range of the x and y axes
    plt.xticks(range(morocco_years.min(), morocco_years.max() + 1, 40))
    plt.yticks(
        range(20, 80, 20), [f"{x}M" for x in range(20, 80, 20)]
    )
    plt.legend()
    # Show the plot
    plt.show()


if __name__ == "__main__":
    main()
