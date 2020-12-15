from array_binary_search import __version__
from array_binary_search.array_binary_search import array_search

test_arr = [4,8,15,16,23,42]
test_term = 15

not_arr = [11,22,33,44,55,66,77]
not_term = 90

def test_version():
    assert __version__ == '0.1.0'

def test_array_search():
    actual = array_search(test_arr,test_term)
    expected = 2
    assert actual == expected

def test_not_found():
    actual = array_search(not_arr,not_term)
    expected = -1
    assert actual == expected