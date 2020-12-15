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
    half = midpoint(arr)
    if arr.index(half) == 1 and half != term:
        return -1
    if half == term:
        return arr.index(half)
    elif half < term:
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

