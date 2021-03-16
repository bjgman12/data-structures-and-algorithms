from hashtable import Hashtable

def test_create():
    hashtable = Hashtable()
    assert hashtable


def test_predictable_hash():
    hashtable = Hashtable()
    initial = hashtable._hash('spam')
    secondary = hashtable._hash('spam')
    assert initial == secondary


def test_in_range_hash():
    hashtable = Hashtable()
    actual = hashtable._hash('spam')

    # assert actual >= 0
    # assert actual < hashtable._size

    assert 0 <= actual < hashtable._size


def test_same_hash():
    hashtable = Hashtable()
    initial = hashtable._hash('listen')
    secondary = hashtable._hash('silent')
    assert initial == secondary


def test_different_hash():
    hashtable = Hashtable()
    initial = hashtable._hash('glisten')
    secondary = hashtable._hash('silent')
    assert initial != secondary

def test_hashtable_add():
    hashtable = Hashtable()
    hashtable.set('glisten',3)

    actual = hashtable.get('glisten')

    expected = 3

    assert actual == expected

def test_hashtable_returns_null():
    hashtable = Hashtable()
    hashtable.set('glisten',3)

    actual = hashtable.get('cat')

    expected = False

    assert actual == expected

def test_hashtable_lookup_collision():
    hashtable = Hashtable()
    hashtable.set('listen',1)
    hashtable.set('silent',2)

    actual = hashtable.get('listen')

    expected = 1


    assert actual == expected

def test_hashtable_contains_true():
    hashtable = Hashtable()
    hashtable.set('listen',1)

    actual = hashtable.contains('listen')
    expected = True

    assert actual == expected

def test_hashtable_contains_true():
    hashtable = Hashtable()
    hashtable.set('listen',1)

    actual = hashtable.contains('listener')
    expected = False

    assert actual == expected
        
