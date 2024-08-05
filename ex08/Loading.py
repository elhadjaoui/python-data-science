
def ft_tqdm(lst: range) -> None:
    """Print the progress of the list processing"""
    for i in lst:
        n = len(lst)
        percentage = (i*100)/(len(lst))
        space_to_fill = (((n - i)*100)//n)
        spaces = ' ' * space_to_fill
        print(f"\r{percentage:.0f}%|{'█'* int(percentage)}{spaces}| ", end="")
        print(f"{i + 1}/{n}", end="")
        yield i


def main():
    lst = range(100)
    # for i in tqdm(range(10000)):
    #     sleep(0.01)
    for i in ft_tqdm(lst):
        percentage = (i*100)/len(lst)
        spaces = ' ' * (int(percentage) - i)
        print(f"\r{percentage:.2f}%|[{'█'* int(percentage)}{spaces}]", end="")
        sleep(0.1)


if __name__ == "__main__":
    """Run the main function"""
    main()

