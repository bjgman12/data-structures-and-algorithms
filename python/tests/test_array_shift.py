
from code_challenges.array_shift.array_shift import array_length
from code_challenges.array_shift.array_shift import modpoint
from code_challenges.array_shift.array_shift import midpoint
from code_challenges.array_shift.array_shift import insert_number

test = [3,4,5,6,7]
insert = 67



def test_array_length():
    actual = array_length(test)
    expected = 5
    assert actual == expected

def test_modpoint():
    actual = modpoint(array_length(test))
    expected = 1
    assert actual == expected

def test_midpoint():
    actual = midpoint(array_length(test),modpoint(array_length(test)))
    expected = 2
    assert actual == expected

def test_insertion():
    actual = insert_number(test, midpoint(array_length(test),modpoint(array_length(test))), insert)
    expected = [3,4,67,5,6,7]
    assert actual == expected