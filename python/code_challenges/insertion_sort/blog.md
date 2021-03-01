# Insertion Sort Break_Down

## function definition
 > You may name your function whatever you like but i would recommend symantecally sound naming, this is a python blog after all. For this demonstration ill go with ...

 - `insert_sort(list_of_ints)`

 > well be passing in an array(list) of ints

 ## Core Logic

 > we will have two place holders or iterator for this implementation we will call these pace and pace-behind

 - `for pace = 1 to len(list_of_ints):`
   - `pace_behind = pace - 1 `
   - `temp = list_of_ints[pace]`
   - `while pace_behind >= 0 and temp < list_of_ints[pace_behind]`
      -`list_of_ints[pace_behind + 1] = list_of_ints[pace_behind]`
      -`pace_behind -= 1`
   -`list_of_ints[pace_behind] = temp`

> this implementation iterates through the array(list) with two variables set to keep track of where it is  and a temp to hold a value that is being moved.

> after we set up our variables we jump into a while loop  that will run its code block as long as pace behind is greater than or equal to zero **AND** while our temp which is **VALUE** of the current index or pace.

> this ensures that one the index of pace-behind is an actual index **AND** that our temp(pace) value is less than the value of the pace_behind index. confirming that we need to move some things around

> once we confirmed that something needs to be moved we have to do the moving

> we do this by first `list_of_ints[pace_behind + 1] = list_of_ints[pace_behind]` setting the value of the index after our pace_behind to pace_behinds indexes value effectively moving the value right one index

> After that we decrement our pace_behind  so the next time the loop iterates it moves value to the left one index right
 

> finally  once pace_behind is less than zero and can no longer reference our list we set `list_of_ints[pace_behind +1] = temp` putting the value that is stored in temp in the front of the list

## STEP THROUGH ITERATION

> Here we will be showing the status of list_of_ints each step of the way to clarify exactly what is happening here.

- We will be using`[8,4,23,16,15]` as our array(list)

> First we call our function

- `insert_sort([8,4,23,16,15])`

> the for loop will begin its first iteration
### pace = 1
- pace_behind is set to pace - 1 `pace_behind = pace -1`
- temp is set to our lists 1 index which is 4 `temp = 4`

> at this point this is the status of our variables
- pace = 1
- pace_behind = 0
- temp = 4
- `[8,4,23,16,15]` hasnt been modified yet

> next we hit our while loop and check its conditions, in our case `pace_behind = 0` which is evaluates to truthy and `temp = 4` which is less than `list_of_ints[pace_behind]` which is **8** since `pace_behind = 0` right now so both of our checks are truthy and we can enter our loop

> slow moving for loop is at 1 fast moving while is on first iteration

> `list_of_ints[pace_behind +1] = list_of_ints[pace_behind]`

> after this executes our list looks like this
- `[8,8,23,42,16,15]`

> next we decrement our pace_behind leaving us
with these current values
- pace = 1
- pace_behind = -1
- temp = 4
- `[8,8,23,42,16,15]`

> with pace_behind being less that zero now we have a falsey value in our while loop check so we exit  and continue to the for loops code block

> here we are setting `list_of_ints[pace_behind + 1] = temp` which leaves our list here and concludes the for loops iteration of pace = 1
- `[4,8,23,42,16,15]`

### pace = 2
> Here we jump to our for loops next iteration with `pace =2`
 - pace = 2
 - pace_behind = 1
 - temp = 23
 - `[4,8,23,42,16,15]`

 > the check for pace behind is truthy but the `temp =23` is not less than  8 so we do not enter our while loop

> list_of_ints[pace_behind + 1] = temp so nothign moves leaving us here for the end of for loop interation at `[pace =2]`

- pace = 2
- pace_behind = 1
- temp = 23
- `[4,8,23,42,16,15]`

### pace = 3
 > here we are going to step through a bit faster

 - pace = 3
 - pace_behind = 2
 - temp = 42

 > 42 is greater than 23, no while loop everything stays put

 - `[4,8,23,42,16,15]`

 ### pace = 4
- pace = 4
- pace_behind = 3
- temp = 16

> while loop check is truthy
 - iteration at pace_behind = 3
   - `[4,8,23,42,42,15]`
   - pace_behind decrements
 - iteration at pace_behind = 2
  - `[4,8,23,23,42,15]`
  - pace_behind decrements
 - exit while loop

> `list_of_ints[pace_behind + 1] = temp`
 - pace = 4
 - pace_behind = 1
 - `[4,8,16,23,42,15]`

### pace = 5
- pace = 5
- pace_behind = 4
- temp = 15

> while loop check is truthy
- itertaion at pace_behind = 4
  - `[4,8,16,23,42,42]`
  - pace_behind decrements
- iteration at pace_behind = 3
  -`[4,8,16,23,23,42]`
  - pace_behind decrements
- iteration at pace_behind = 2
  - `[4,8,16,16,23,42]`
  - pace_behind decrements
- exit while loop

> `list_of_int[pace_behind + 1] = temp`
- `[4,8,15,16,23,42]` fully sorted