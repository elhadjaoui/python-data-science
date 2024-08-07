
def ft_tqdm(lst: range) -> None:
    """ft_tqdm function simulate the tqdm function from the tqdm library
    it takes a range and print the progress of the iteration
    Args:
        lst (range): the range of the iteration
    Returns:
        None
    """
    for i in lst:
        n = len(lst)
        percentage = (i*100)/(len(lst))
        space_to_fill = (((n - i)*100)//n)
        spaces = ' ' * space_to_fill
        print(f"\r{percentage:.0f}%|{'█'* int(percentage)}{spaces}| ", end="")
        print(f"{i + 1}/{n}", end="")
        yield i


def main():
    """Main function"""
    for _ in ft_tqdm(range(333)):
        pass


if __name__ == "__main__":
    """Run the main function"""
    main()
