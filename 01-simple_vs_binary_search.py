import math
import random


def binary_search(arr, item):
    """
    Only works when we get an ordered list.
    """
    if not list or len(arr) == 0:
        return None

    low = arr[0]
    high = arr[-1]

    while low <= high:
        mid = (low + high) // 2
        if mid == item:
            return mid
        if item < mid:
            high = mid - 1
        if item > mid:
            low = mid + 1

    return None

def simple_search(arr, item):
    if not list or len(arr) == 0:
        return None

    for i in arr:
        if i == item:
            return i

    return None


if __name__ == '__main__':
    my_arr = list(range(10, 10_000, 5))
    my_item = 8_005
    print(binary_search(my_arr, my_item))
    print(simple_search(my_arr, my_item))

