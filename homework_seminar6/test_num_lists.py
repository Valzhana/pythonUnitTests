
# Данные сценарии тестирования выбраны потому, что в них высока вероятность ошибок.


"""List Averages Comparison"""

import pytest

from homework_seminar6.num_lists import NumsLists


@pytest.fixture
def list1():
    """Fixture for providing data for test"""
    return [2, 3, 1, 1, 3]


@pytest.fixture
def list2():
    """Fixture for providing data for test"""
    return [1, 7, 3, 4, 5]


def test_init(list1, list2):
    """Checking for correct class initialization"""
    nums_list = NumsLists(list1, list2)
    assert nums_list.lst1 == list1
    assert nums_list.lst2 == list2


def test_get_lists_averages(list1, list2):
    """Checking lists averages consisting of several elements"""
    nums_list = NumsLists(list1, list2)
    assert nums_list.get_lists_averages() == (2, 4)


@pytest.mark.parametrize('lst1, lst2, expected',
                         [([2, 4, 3], [], (3, 0)),
                          ([], [1, 3, 2], (0, 2)),
                          ([], [], (0, 0))])
def test_empty_lists_averages(lst1, lst2, expected):
    """Checking averages if one or both lists are empty"""
    nums_list = NumsLists(lst1, lst2)
    assert nums_list.get_lists_averages() == expected


@pytest.mark.parametrize('lst1, lst2, expected',
                         [([5], [0], (5, 0)),
                          ([5, 1, 2, 1, 1], [7], (2, 7)),
                          ([4], [4, 6], (4, 5))])
def test_one_element_lists_averages(lst1, lst2, expected):
    """Checking averages if one or both lists have only one element"""
    nums_list = NumsLists(lst1, lst2)
    assert nums_list.get_lists_averages() == expected


def test_first_list_average_is_greater(list1, list2, capfd):
    """Checking the message when the average value of the first list is greater"""
    nums_list = NumsLists(list2, list1)
    nums_list.compare_averages()
    captured = capfd.readouterr()
    assert captured.out.strip() == 'The first list has a higher average value'


def test_second_list_average_is_greater(list1, list2, capfd):
    """Checking the message when the average value of the second list is greater"""
    nums_list = NumsLists(list1, list2)
    nums_list.compare_averages()
    captured = capfd.readouterr()
    assert captured.out.strip() == 'The second list has a higher average value'


def test_equal_averages(list1, capfd):
    """Checking the message when the average values of the lists are equal"""
    nums_list = NumsLists(list1, list1)
    nums_list.compare_averages()
    captured = capfd.readouterr()
    assert captured.out.strip() == 'The averages are equal'


if __name__ == '__main__':
    pytest.main(['-v'])
