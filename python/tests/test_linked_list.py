
from data_structures.linked_list.linked_list import LinkedList, Node


def test_import():
    assert LinkedList


def test_void():
    linked = LinkedList()
    actual = linked.insert(Node(None))
    value = None
    assert actual == value

node = Node(6)
linked = LinkedList(node)

def test_head():
    actual = linked.head.value
    expected = 6
    assert actual == expected

def test_insert():
    newNode = Node(12)
    linked.insert(newNode.value)
    actual = linked.head.value
    expected = 12
    assert actual == expected

    actual = linked.head.next.value
    expected = 6
    assert actual == expected

def test_search():

    linked.insert(15)
    linked.insert(11)
    actual = linked.inside(15)
    expected = True
    assert actual == expected

def test_str():
    node = Node(9)
    linked_test = LinkedList(node)
    linked_test.insert(8)
    linked_test.insert(7)
    linked_test.insert(6)

    actual = str(linked_test)
    expected = '{6} -> {7} -> {8} -> {9} -> Null'

    assert actual == expected

def test_insertBefore():
    node = Node(6)
    linked1 = LinkedList(node)
    linked1.insert(5)
    linked1.insert(4)
    linked1.insertBefore(5,9)

    actual = str(linked1)
    expected = '{4} -> {9} -> {5} -> {6} -> Null'

    assert actual == expected


def test_insertAfter():
    node = Node(6)
    linked2 = LinkedList(node)
    linked2.insert(5)
    linked2.insert(4)
    linked2.insertAfter(5,9)

    actual = str(linked2)
    expected = '{4} -> {5} -> {9} -> {6} -> Null'

    assert actual == expected