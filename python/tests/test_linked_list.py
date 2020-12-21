
from data_structures.linked_list.linked_list import LinkedList, Node
import pytest

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
    linked.insert(7)
    linked.insert(8)
    linked.insert(9)

    actual = str(linked)
    expected = '{6} -> {7} -> {8} -> {9} -> Nullp'