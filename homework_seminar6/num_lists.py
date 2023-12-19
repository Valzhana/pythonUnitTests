"""List Averages Comparison"""


class NumsLists:
    """Is a class NumsLists."""

    def __init__(self, lst1: list[int], lst2: list[int]):
        """Class initialization."""

        self.lst1 = lst1
        self.lst2 = lst2

    def get_lists_averages(self):
        """Calculate the averages of first and second lists"""
        avg1 = 0
        if self.lst1:
            avg1 = sum(self.lst1) / len(self.lst1)

        avg2 = 0
        if self.lst2:
            avg2 = sum(self.lst2) / len(self.lst2)

        return avg1, avg2

    def compare_averages(self) -> None:
        """Function, that compares the averages of two lists"""
        avg1, avg2 = self.get_lists_averages()

        if avg1 > avg2:
            print('The first list has a higher average value')
        elif avg1 < avg2:
            print('The second list has a higher average value')
        else:
            print('The averages are equal')
