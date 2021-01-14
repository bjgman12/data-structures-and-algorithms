class InvalidOperationError(BaseException):
    pass


class Node():
    def __init__(self,value,next = None):
        self.value = value
        self.next = next

class Stack():

    def __init__(self,node = None):
        self.top = node

    def __str__(self):
        curr = self.top
        display = 'Null'
        while curr:
            display += f' <- {curr.value} '
            curr = curr.next
        return display


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

class PseudoQueue():

    def __init__(self,stack_one = None,stack_two = None):
        self.front = None
        self.rear = None
        self.stack_one = Stack()
        self.stack_two = Stack()

    def enqueue(self,value,stack = None):
        """
        can enqueue and or push into a stack

        Args:
            value (int): [thing to be added to collection]
            stack ([stack], optional): [description] tells method whic stack to operate on. Defaults to None.
        """
        insert_Node = Node(value)
        if stack:
            self.rear = stack.top
            stack.push(value)

        if self.is_empty():
            self.front = insert_Node
            self.rear = insert_Node
        else:
            self.rear.next = insert_Node
            self.rear = insert_Node

    def dequeue(self,stack):
        """[summary]

        Args:
            stack ([type]): [description]

        Returns:
            [type]: [description]
        """
        retval = 0
        saved = []
        if stack:
            self.rear = stack.top
            current = self.rear

            
            while current.next is not None:
                saved.append(current.value)
                stack.pop()
                current = current.next

            retval = current 
            
            stack.pop()

            while saved:
                stack.push(saved.pop(-1))
            

        return retval.value

    def peek(self):
        if self.is_empty():
            raise InvalidOperationError("Method not allowed on empty collection")
        return self.front.value


    def is_empty(self):
        if self.front is None:
            return True
        return False
      

if __name__ == "__main__":
     pq = PseudoQueue()
     pq.stack_one.push(3)
     pq.stack_one.push(4)
     pq.stack_one.push(5)

     print(pq.stack_one)
     pq.enqueue(6,pq.stack_one)
     print(pq.stack_one)
     print(pq.dequeue(pq.stack_one))
     print(pq.stack_one)


    
