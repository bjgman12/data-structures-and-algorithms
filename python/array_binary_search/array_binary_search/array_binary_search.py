latter_arr = [1,2,3,4,5,6,7]
term = 5


test_arr = [4,8,15,16,23,42]
test_term = 15

saved_arr = []

def midpoint(arr):
    middle = float(len(arr)/2)
    if (middle % 2):
        return arr[int(middle -.5)]
    else:
        return arr[int(middle)]
    """[summary]
    function takes in an array and returns the mid point 
    odd or even
    """
  

def array_search(arr,term):
    print(arr)
    global saved_arr
    if arr == []:
        return -1

    if (len(arr) == 3):
        for item in arr:
            if (item == term):
                return saved_arr.index(term)

    half = midpoint(arr)
    if arr.index(half) == 1 and half != term:
        return -1
    if half == term:
        if(saved_arr):
            return saved_arr.index(half)
        else:
            return arr.index(half)
    elif half < term:
        saved_arr = arr
        print(saved_arr)
        slicedArr = arr[arr.index(half):-1]
        return array_search(slicedArr,term)
    elif half > term:
        slicedArr = arr[0:arr.index(half)]
        return array_search(slicedArr,term)
    """[summary]
    this function takes in and array and search term
    uses mid point to cut the array in half then recursively
    calls itself until either it finds the number to determines 
    the number is not in the list
    """

print(array_search(test_arr,15))