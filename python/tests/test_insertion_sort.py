from code_challenges.insertion_sort.insertion_sort import insert_sort

def test_sorting_functionality():
    test_list = [8,4,23,42,16,15]
    actual = insert_sort(test_list)
    expected = [4,8,15,16,23,42]
    assert actual == expected

