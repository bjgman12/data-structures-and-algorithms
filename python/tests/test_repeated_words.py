from code_challenges.repeated_word.repeated_word import repeated_word_check

def test_repeated_a():
   actual = repeated_word_check('a nice day to be a dev')
   expected = 'a'

   assert actual == expected

def test_no_repeat():
    actual = repeated_word_check('it is a nice day')
    expected = 'No Words Repeated'

    assert actual == expected

def test_longer_string():
    actual = repeated_word_check('here we are going to call our function Merge_Sort and we will be passing in the array tht we want it to sort expecting it to return a sorted array and another function to call recursively called merge that takes in the left side the right side and the original array')
    expected = 'we'

    assert actual == expected

def test_same_hash():
    actual = repeated_word_check('cat can act but cat cant tac')
    expected = 'cat'

    assert actual == expected

def test_string_format():
    actual = repeated_word_check('It was the best of times, it was the worst of times, it was the age of wisdom, it was the age of foolishness, it was the epoch of belief, it was the epoch of incredulity, it was the season of Light, it was the season of Darkness, it was the spring of hope, it was the winter of despair, we had everything before us, we had nothing before us, we were all going direct to Heaven, we were all going direct the other way – in short, the period was so far like the present period, that some of its noisiest authorities insisted on its being received, for good or for evil, in the superlative degree of comparison only...')
    expected = 'it'

    assert actual == expected