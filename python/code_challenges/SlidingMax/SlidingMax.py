## Sliding Window Approach


def sub_max(arr,k):
    """[returns the max subarray sum of size k]

    Args:
        arr ([arr]): [list to operate on]
        k ([int]): [subarray size]

    Returns:
        [int]: [max subarray sum]
    """
    if not arr:
        return 0
    max_sum, window_sum = 0, 0
    window_start = 0

    for window_end in range(len(arr)):
        window_sum += arr[window_end]
        if window_end >= (k-1):
            max_sum = max(max_sum,window_sum)
            window_sum -= arr[window_start]
            window_start +- 1
    return max_sum