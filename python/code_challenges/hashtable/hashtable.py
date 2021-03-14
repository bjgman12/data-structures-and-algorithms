from linked_list import Node, LinkedList

class Hashtable:

    def __init__(self,_size=1024):
        self._size = _size
        # creates a size about of buckets and assignes them to none
        self._buckets = _size * [None]

    def _hash(self,key):
        
        # will need to factor length
        # max index in hash table length - 1
        # >= 0
        sum = 0

        for ch in key:
            sum += ord(ch) # ord converts to ascii values
        
        primed = sum * 19
        index = primed % self._size

        return index

    



    def set(self,key,value):
        # hash they key
        hashed_key_index = self._hash(key)

        # determine if the bucket is empty
        # if its empty create ll then if not then add
        if not self._buckets[hashed_key_index]:
            self._buckets[hashed_key_index] = LinkedList()
        
        self._buckets[hashed_key_index].insert((key,value))

      
        

    def get(self,requested_key):
        #TODO:
        #takes in a key and returns the value 
        requested_index = self._hash(requested_key)
        # assign bucket to temp variable
        temp_bucket = self._buckets[requested_index]
        #check if index is empty or not
        if temp_bucket:
            current = temp_bucket.head
            while current:
                if current.value[0] == requested_key:
                    return current.value[1]
                else:
                    current = current.next
            return False
        return False
        # assign something to head of LL
        # (key,value) this is the value of each LL node
        #current.value[0]= key
        #current.valuep[0] = value
        # if key matches requested key then return value
        # else  go to .next until key is found or end of ll


    def contains(self,requested_key):
        return bool(self.get(requested_key))