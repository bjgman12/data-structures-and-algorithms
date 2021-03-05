# Merge_Sort Break_Down

## function definition
 > here we are going to call our function Merge_Sort and we will be passing in the array tht we want it to sort expecting it to return a sorted array and another function to call recursively called merge that takes in the left side the right side and the original array

 -`merge_sort(arr)`

 ## Core Logic

 > first we will set a variable and store the length of the array inside it this will be used to determin a mid point

 -`n = len(arr)`

 > after that we will check if the lists length is longer than one meaning there is actually something to be sorted there.

 - `if  n >  1 :`

 > inside this code block we declare the mid point as well as the left and right sides of our original array we do this by

 - `mid = n/2` > you can add int here to handle odd length arrays note that one side will be longer in this case by one

 -`left_side = arr[0-mid]` 
 -`right_side = arr[mid-n]`