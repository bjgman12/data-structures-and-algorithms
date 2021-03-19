from .tree import BinaryNode,BinaryTree


def tree_intersection(tree_one,tree_two):
    """[given two binarytrees as parameters returns the itersection of the trees values]

    Args:
        tree_one ([binarytree]): [description]
        tree_two ([binarytree]): [description]

    Returns:
        [list]: [intersection of trees]
    """
    intersection = []
    for item in tree_two.breadth_first():
        if item in tree_one.breadth_first():
            intersection.append(item)

    return intersection
