class InvalidOperationError(BaseException):
    pass

class Node():
    def __init__(self,value,next = None):
        self.value = value
        self.next = next
class Queue():
    
    def __init__(self):
        self.front = None
        self.rear = None

    def enqueue(self,value):
        insert_Node = Node(value)

        if self.is_empty():
            self.front = insert_Node
            self.rear = insert_Node
        else:
            self.rear.next = insert_Node
            self.rear = insert_Node

    def dequeue(self):
        if self.is_empty():
            raise InvalidOperationError("Method not allowed on empty collection")
        ret_val = self.front.value

        self.front = self.front.next

        return ret_val

    def peek(self):
        if self.is_empty():
            raise InvalidOperationError("Method not allowed on empty collection")
        return self.front.value


    def is_empty(self):
        if self.front is None:
            return True
        return False

class BinaryNode():
      def __init__(self,value,left = None,right= None):
        self.value = value
        self.left = left
        self.right = right

class BinaryTree:
  def __init__(self,node = None):
    self.root = node
    self.collect = []
    self.max = 0

    self.breadth_first()
        
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

  def max_value(self):
    def traverse(root):
      if root.value > self.max:
        self.max = root.value
      if root.left:
        traverse(root.left)
      if root.right:
        traverse(root.right)
    traverse(self.root)
    return self.max

  def breadth_first(self):
        ret_val = []
        breadth_q = Queue()
        breadth_q.enqueue(self.root)

        current = breadth_q.dequeue()
        while current:
          if current.left:
            breadth_q.enqueue(current.left)
          if current.right:
            breadth_q.enqueue(current.right)
          ret_val.append(current.value)
          if breadth_q.is_empty():
            current = None
          else:
            current = breadth_q.dequeue()
            
                
        return ret_val
          
                

class BinarySearchTree(BinaryTree):
  # def __init__(self, root = None):
  #   super().__init__(root)
  
  @staticmethod
  def add(tree,value):
    def add_search(root,value):
      if not root:
        return BinaryNode(value)
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

  #  a = BinaryNode(4)
  #  b = BinaryNode(8)
  #  c = BinaryNode(15)
  #  d = BinaryNode(16)
  #  e = BinaryNode(22)
  #  f = BinaryNode(23)
  #  g = BinaryNode(27)
  #  h = BinaryNode(42)
  #  i = BinaryNode(85)
  #  j = BinaryNode(105)

  #  tree.root = a
  #  tree.root.left = b
  #  tree.root.right = c


  #  tree = BinaryTree(f)

  #  tree.root.left = b
  #  tree.root.right = h

  #  b.left = a
  #  b.right = d

  #  d.left = c
  #  d.right = e

  #  h.left = g
  #  h.right = i

  #  i.right = j

  #  tree.in_order()
  #  tree.post_order()
  #  tree.pre_order()
  #  BinarySearchTree.add(tree,5)
  #  BinarySearchTree.add(tree,100)
  #  tree.in_order()
  #  print(BinarySearchTree.contains(tree.root,5))


   a = BinaryNode(1)
   b = BinaryNode(3)
   c = BinaryNode(4)
   d = BinaryNode(2)
   e = BinaryNode(7)

   tree = BinaryTree(a)
   
   tree.root.left = b
   tree.root.right = c

   c.left = d
   c.right = e

   print(tree.breadth_first())


