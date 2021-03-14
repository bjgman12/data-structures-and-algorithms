# from code_challenges.fizz_buzz_tree.fizz_buzz_tree import Node, KaryNode,KaryTree,Queue,fbt

# def test_fbt():
#     one = KaryNode(1)
#     two = KaryNode(2)
#     three = KaryNode(3)
#     four = KaryNode(4)
#     five = KaryNode(5)
#     six = KaryNode(6)
#     seven = KaryNode(7)
#     eight = KaryNode(8)
#     nine = KaryNode(9)
#     ten = KaryNode(10)
#     eleven = KaryNode(11)
#     twelve = KaryNode(12)
#     thirteen = KaryNode(13)
#     fourteen = KaryNode(14)
#     fifteen = KaryNode(15)

#     #ones children
#     one.children.append(two)
#     one.children.append(three)
#     one.children.append(five)

#     #twos children
#     two.children.append(four)
#     two.children.append(seven)
#     two.children.append(eight)
#     two.children.append(eleven)
#     two.children.append(thirteen)
#     two.children.append(fourteen)
#     two.children.append(fifteen)

#     #threes children
#     three.children.append(six)
#     three.children.append(nine)
#     three.children.append(twelve)

#     #fives children
#     five.children.append(ten)

#     tree = KaryTree(one)

#     actual = fbt(tree)
#     expected = ['1', '2', 'Fizz', 'Buzz', '4', '7', '8', '11', '13', '14', 'FizzBuzz', 'Fizz', 'Fizz', 'Fizz', 'Buzz']

#     assert actual == expected