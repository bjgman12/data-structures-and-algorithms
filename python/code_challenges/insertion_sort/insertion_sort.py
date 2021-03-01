def insert_sort(unsorted_list):
    """[Takes in an unsorted list and returns a sorted list]
    Args:
        unsorted_list ([list]): [an unsorted list of ints]
    """
    pace = 1
    for pace in range(len(unsorted_list)):
        pace_behind = pace - 1
        temp = unsorted_list[pace]

        while pace_behind >=0 and temp < unsorted_list[pace_behind]:
            unsorted_list[pace_behind + 1] = unsorted_list[pace_behind]
            pace_behind -= 1

        unsorted_list[pace_behind + 1] = temp
    
    return unsorted_list
    