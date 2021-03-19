from code_challenges.tree_intersection.tree_intersection import tree_intersection
from code_challenges.tree_intersection.tree_intersection import BinaryNode,BinaryTree

def test_intersection_returns():
    tree_one = BinaryTree(BinaryNode(5,BinaryNode(4,BinaryNode(1)),BinaryNode(3)))
    tree_two = BinaryTree(BinaryNode(2,BinaryNode(4,BinaryNode(1)),BinaryNode(6)))

    actual = tree_intersection(tree_one,tree_two)
    expected = [4,1]

    assert actual == expected

def test_no_intersections():
    tree_one = BinaryTree(BinaryNode(5,BinaryNode(4,BinaryNode(1)),BinaryNode(3)))
    tree_two = BinaryTree(BinaryNode(9,BinaryNode(8,BinaryNode(7)),BinaryNode(6)))

    actual = tree_intersection(tree_one,tree_two)
    expected = []

    assert actual == expected
    
def test_different_types():
    tree_one = BinaryTree(BinaryNode(5,BinaryNode('match',BinaryNode(1)),BinaryNode(3)))
    tree_two = BinaryTree(BinaryNode(9,BinaryNode(8,BinaryNode(1)),BinaryNode('match')))

    actual =  tree_intersection(tree_one,tree_two)
    expected = ['match',1]
    assert actual == expected