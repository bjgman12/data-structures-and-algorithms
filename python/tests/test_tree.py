import pytest
from data_structures.tree.tree import Node, BinaryTree, BinarySearchTree

def test_empty_tree():
    
    tree = BinaryTree()
    actual = tree.root
    expected = None
    assert actual == expected
def test_root_only():
    node = Node(23)
    tree = BinaryTree(node)
    actual = tree.root.value
    expected = 23
    assert actual == expected

def test_root_right_left():
    node = Node(23)
    tree = BinaryTree(node)
    BinarySearchTree.add(tree,8)
    BinarySearchTree.add(tree,42)

    actual = tree.root.left.value
    expected = 8
    assert actual == expected

    actual = tree.root.right.value
    expected = 42
    assert actual == expected

def test_in_order_collection():
    node = Node(23)
    tree = BinaryTree(node)
    BinarySearchTree.add(tree,8)
    BinarySearchTree.add(tree,42)
    BinarySearchTree.add(tree,9)
    BinarySearchTree.add(tree,10)
    BinarySearchTree.add(tree,5)

    tree.in_order()
    actual = tree.collect
    expected = [5,8,9,10,23,42]
    assert actual == expected

def test_post_order_collection():
    node = Node(23)
    tree = BinaryTree(node)
    BinarySearchTree.add(tree,8)
    BinarySearchTree.add(tree,42)
    BinarySearchTree.add(tree,9)
    BinarySearchTree.add(tree,10)
    BinarySearchTree.add(tree,5)

    tree.post_order()
    actual = tree.collect
    expected = [5,10,9,8,42,23]
    assert actual == expected

def test_pre_order_collection():
    node = Node(23)
    tree = BinaryTree(node)
    BinarySearchTree.add(tree,8)
    BinarySearchTree.add(tree,42)
    BinarySearchTree.add(tree,9)
    BinarySearchTree.add(tree,10)
    BinarySearchTree.add(tree,5)

    tree.pre_order()
    actual = tree.collect
    expected = [23,8,5,9,10,42]
    assert actual == expected

def test_max_value():
    node = Node(23)
    tree = BinaryTree(node)
    BinarySearchTree.add(tree,8)
    BinarySearchTree.add(tree,42)
    BinarySearchTree.add(tree,9)
    BinarySearchTree.add(tree,10)
    BinarySearchTree.add(tree,5)

    actual = tree.max_value()
    expected = 42
    assert actual == expected