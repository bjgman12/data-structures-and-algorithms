
test = [3,4,5,6,7]
insert = 67



def array_length(arr):
    return len(test)


def modpoint(arr_length):
    mid = (arr_length % 2)
    return mid

def midpoint( arr_length, mod_point):
    if (mod_point == 1):
       mid_point = (arr_length - 1)/2
    else:
        mid_point = arr_length/2
    return int(mid_point)

def insert_number(arr,index,insert_num):
    arr.insert(index,insert_num)
    return arr

