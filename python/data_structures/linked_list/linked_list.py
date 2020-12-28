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

    def append(self,value):
        """
        This function sets the current to the head value
        and then set it equal to the next node if traverses
        through the linked lsit untill there is no next value
        and then sets a new next to current after escaping
        the loop it makes a new next and stores our value inside
        """
        current = self.head
        if current:
            while current.next != None:
                current = current.retNext()
            current.next = Node(value)
        else:
            self.head = Node(value)

    def insertAfter(self,chosen,value):
        
        current = self.head
      
        if current.next is chosen:
            self.insert(value)
            return 
        
        while current is not None:
            if current.next is chosen:
                new_node = Node(value)
                new_node.next = current.next
                current.next = node
                return 
            current = current.next
            
    

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
    linked.append(20)
    linked.insertAfter(15,16)
    print(linked)