class Node():
      def __init__(self,value,left = None,right= None):
        self.value = value
        self.left = left
        self.right = right

class BinaryTree:
  def __init__(self,node = None):
    self.root = node
    self.collect = []
        
  def pre_order(self):
    def traverse(root):
    # print root
     self.collect.append(root.value)
    # traverse left
    # traverse right
     if root.left:
      traverse(root.left)
     if root.right:
       traverse(root.right)
    traverse(self.root)

  def in_order(self):
    def traverse(root):
      if root.left:
        traverse(root.left)
        
      self.collect.append(root.value)
        

      if root.right:
        traverse(root.right)
    traverse(self.root)

  def post_order(self):
    def traverse(root):

      if root.left:
        traverse(root.left)

      if root.right:
        traverse(root.right)
    
      self.collect.append(root.value)
    traverse(self.root)

class BinarySearchTree(BinaryTree):
  # def __init__(self, root = None):
  #   super().__init__(root)
  
  @staticmethod
  def add(tree,value):
    def add_search(root,value):
      if not root:
        return Node(value)
      else:
        if root.value == value:
          print('raise exception alreay in tree')
        elif root.value < value:
          root.right = add_search(root.right,value)
        else:
          root.left = add_search(root.left,value)
      return root
    add_search(tree.root,value)

  @staticmethod
  def contains(root,value):
      while root:
        if root.value == value:
          return True
        elif root.value > value:
          root = root.left
        elif root.value < value:
          root = root.right
      return False

    



if __name__ == "__main__":
  # set a as root
  # set left of a to b
  # set right of a to c

  # tree = BinaryTree()

   a = Node(4)
   b = Node(8)
   c = Node(15)
   d = Node(16)
   e = Node(22)
   f = Node(23)
   g = Node(27)
   h = Node(42)
   i = Node(85)
   j = Node(105)

  #  tree.root = a
  #  tree.root.left = b
  #  tree.root.right = c


   tree = BinaryTree(f)

   tree.root.left = b
   tree.root.right = h

   b.left = a
   b.right = d

   d.left = c
   d.right = e

   h.left = g
   h.right = i

   i.right = j

  #  tree.in_order()
  #  tree.post_order()
  #  tree.pre_order()
   BinarySearchTree.add(tree,5)
   BinarySearchTree.add(tree,100)
   tree.in_order()
   print(BinarySearchTree.contains(tree.root,5))