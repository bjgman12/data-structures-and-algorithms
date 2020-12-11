from array_shift import __version__
from array_shift.array_shift import array_length
from array_shift.array_shift import modpoint
from array_shift.array_shift import midpoint
from array_shift.array_shift import insert_number

test = [3,4,5,6,7]
insert = 67

def test_version():
    assert __version__ == '0.1.0'

def test_array_length():
    actual = array_length(test)
    expected = 5
    assert actual == expected

def test_modpoint():
    actual = modpoint(test)
    expected = 1
    assert actual == expected

def test_midpoint():
    actual = midpoint(array_length(test),modpoint(test))
    expected = 2
    assert actual == expected

def test_insertion():
    actual = insert_number(test, midpoint(array_length(test),modpoint(test)), insert)
    expected = [3,4,67,5,6,7]
    assert actual == expected