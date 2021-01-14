class InvalidOperationError(BaseException):
    pass

class Node():
    def __init__(self,value,next = None):
        self.value = value
        self.next = next

class AnimalShelter():
    
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

    def enqueue(self,animal):
        if (animal != 'dog' and animal !='cat'):
            raise InvalidOperationError('Value must be of proper animal type')
        insert_Node = Node(animal)

        if self.is_empty():
            self.front = insert_Node
            self.rear = insert_Node
        else:
            self.rear.next = insert_Node
            self.rear = insert_Node

    def dequeue(self,animal = None):
        if self.is_empty():
            raise InvalidOperationError("Method not allowed on empty collection")
        if animal != 'dog' and animal != 'cat':
            ret_val = self.front
            self.front = self.front.next
            return ret_val
        
        type_check = self.front

        if type_check == animal:
            ret_val = type_check.value
            self.front = self.front.next
            return ret_val
        else:
            while type_check.next.value is not animal:
                type_check = type_check.next

        ret_val = type_check.next.value

        type_check.next = type_check.next.next


        return ret_val

    def peek(self):
        if self.is_empty():
            raise InvalidOperationError("Method not allowed on empty collection")
        return self.front.value


    def is_empty(self):
        if self.front is None:
            return True
        return False


if __name__ == "__main__":
    shelter = AnimalShelter()
    shelter.enqueue('dog')
    shelter.enqueue('dog')
    shelter.enqueue('cat')
    shelter.enqueue('dog')
    shelter.enqueue('cat')


    shelter.dequeue('cat')
    print(str(shelter))