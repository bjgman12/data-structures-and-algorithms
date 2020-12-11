
test = [3,4,5,6,7]
insert = 67

def array_length(test):
    return len(test)

def modpoint( length = array_length(test)):
    mid = (length % 2)
    return mid
    # if ( mid = 0)
    # return mid

def midpoint( length = array_length(test),  mod = modpoint(test)):
    if (mod == 1):
        (length - 1)/2
    else:
        mid = length/2
    
    return mid

def insert_number(arr,index = midpoint(lenght = array_length, mod = modpoint(test)), insert):
    arr.insert(index,insert)
    return arr
    