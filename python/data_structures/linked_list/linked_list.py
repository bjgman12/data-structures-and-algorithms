class Node:
    def __init__(self,value,next = None):
        self.value = value
        self.next = next

    def retVal(self):
        return self.value
    
    def retNext(self):
        return self.next

class LinkedList:
    """
    Put docstring here
    """
    def __init__(self,head = None, values = None):
        self.head = head

    def insert(self,value):
        node = Node(value)

        node.next = self.head

        self.head = node

    def inside(self, value):
        curr = self.head

        while curr is not None:

            if curr.retVal() == value:
                return True
            else:
                curr = curr.retNext()
        return False

    def __str__(self):
        curr = self.head
        display = ''

        while curr is not None:
            display += f' { {curr.value} } ->'

            curr = curr.next
        
        display += ' Null '
        return display

if __name__ == "__main__":
    node = Node(12)
    linked = LinkedList(node)
    linked.insert(14)
    linked.insert(15)
    linked.insert(11)
    print(linked)