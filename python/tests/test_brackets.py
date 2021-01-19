from code_challenges.multi_bracket_validation.multi_bracket_validation import multi_bracket_validation

def test_balance_one():
    actual = multi_bracket_validation('[](){}')
    expected = True
    assert actual == expected

def test_balance_two():
    actual = multi_bracket_validation('[()]{}')
    expected = True
    assert actual == expected

def test_balance_three():
    actual = multi_bracket_validation('[(]){}')
    expected = False
    assert actual == expected



