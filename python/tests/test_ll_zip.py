from code_challenges.ll_zip.ll_zip.ll_zip import Node,LinkedList

def test_import():
    assert LinkedList

def test_ll_zip():
    linked = LinkedList()
    linked.insert(5)
    linked.insert(3)
    linked.insert(1)

    linked2 = LinkedList()
    linked2.insert(6)
    linked2.insert(4)
    linked2.insert(2)

    actual = str(linked.ll_zip(linked,linked2))
    expected = '{1} -> {2} -> {3} -> {4} -> {5} -> {6} -> Null'
    assert actual == expected