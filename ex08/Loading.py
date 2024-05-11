from time import sleep


def ft_tqdm(lst: range) -> None:
    """Print the progress of the list processing"""
    for i in lst:
        yield i


def main():
    lst = range(1000)
    for i in ft_tqdm(lst):
        percentage = (i*100)/len(lst)
        spaces = " " * (int(percentage) - i)
        print(f"\r{percentage:.2f}%|[{'='* int(percentage)}{spaces}]", end="")
        sleep(0.1)


if __name__ == "__main__":
    """Run the main function"""
    main()



# for i in range(21):
#     spaces = " " * (20 - i)
#     percentage = 5*i
#     print(f"\r[{'='*i}{spaces}]{percentage}%", flush=True, end="")
#     sleep(0.25)
   
    # countdown.py

print(f"{'Countdown':^20}")

# for second in range(3, 0, -1):
#     print(second, flush=True, end=" ")
#     sleep(1)
# print("Go!")