
from code_challenges.array_binary_search.array_binary_search import array_search

test_arr = [4,8,15,16,23,42]
test_term = 15

not_arr = [11,22,33,44,55,66,77]
not_term = 90

empty = []

latter_arr = [1,2,3,4,5,6,7]
term = 5

saved_arr = []



def test_array_search():
    actual = array_search(test_arr,test_term)
    expected = 2
    assert actual == expected

def test_not_found():
    actual = array_search(not_arr,not_term)
    expected = -1
    assert actual == expected

def test_empty():
    actual = array_search(empty,not_term)
    expected = -1
    assert actual == expected

def test_latter_half():
    actual = array_search(latter_arr,term)
    expected = 4
    assert actual == expected

def test_latter_half_6():
    actual = array_search(latter_arr,6)
    expected = 5
    assert actual == expected