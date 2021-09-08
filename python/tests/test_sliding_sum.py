from code_challenges.SlidingMax.SlidingMax import sub_max



def test_output():
    actual = sub_max([2,1,5,2,3,3],3)
    expected = 10
    assert actual == expected 

def test_empty_array():
    actual = sub_max([],3)
    expected = 0 
    assert actual == expected

def test_negatives():
    actual = sub_max([-1,0,2,-1,-1],3)
    expected = 1
    assert actual == expected
