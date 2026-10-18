from sorting.selection_sort import selection_sort


def test_empty_list():
 assert selection_sort([]) == []


def test_single_element():
 assert selection_sort([42]) == [42]


def test_already_sorted():
 assert selection_sort([1, 2, 3, 4, 5]) == [1, 2, 3, 4, 5]


def test_reverse_sorted():
 assert selection_sort([5, 4, 3, 2, 1]) == [1, 2, 3, 4, 5]


def test_duplicates():
 assert selection_sort([3, 1, 2, 3, 1]) == [1, 1, 2, 3, 3]


def test_does_not_mutate_input():
 original = [5, 3, 1, 4, 2]
 copy = list(original)
 selection_sort(original)
 assert original == copy


def test_negative_numbers():
 assert selection_sort([-3, -1, -2, 0, 2]) == [-3, -2, -1, 0, 2]
