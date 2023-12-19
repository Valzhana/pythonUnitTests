from homework_seminar6.num_lists import NumsLists


def main():

    num_lists = NumsLists([1, 2, 3], [4, 5, 6])
    averages = num_lists.get_lists_averages()

    print(f"The average of list 1 is: {averages[0]}")
    print(f"The average of list 2 is: {averages[1]}")
    num_lists.compare_averages()


if __name__ == "__main__":
    main()
