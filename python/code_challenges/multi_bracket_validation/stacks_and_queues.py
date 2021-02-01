class InvalidOperationError(BaseException):
    pass

class Node():
    def __init__(self,value,next = None):
        self.value = value
        self.next = next

class Stack():

    def __init__(self,node = None):
        self.top = node

    def push(self,value):
        insert_Node = Node(value)

        insert_Node.next = self.top

        self.top = insert_Node
        
    def pop(self):
        if self.is_empty():
           raise InvalidOperationError("Method not allowed on empty collection")

        node = self.top
        self.top = self.top.next

        return node.value

    def peek(self):
        if self.is_empty():
            raise InvalidOperationError("Method not allowed on empty collection")
        return self.top.value
    
    def is_empty(self):
        if self.top is None:
            return True
        
        return False

class Queue():

    def __init__(self):
        self.front = None
        self.rear = None


    def __str__(self):
        curr = self.front
        display = ''
        while curr:
            display += f'{curr.value} -> '
            curr = curr.next
        display += 'Null'
        return display


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