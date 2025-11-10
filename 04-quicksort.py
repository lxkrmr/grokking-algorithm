def binary_search(arr, item):
    return _binary_search_rec(item, arr[0], arr[-1])


def _binary_search_rec(item, low, high):
    if low > high:
        return None

    mid = (low + high) // 2
    if mid == item:
        return mid

    if item < mid:
        return _binary_search_rec(item, low, mid - 1)
    else:
        return _binary_search_rec(item, mid + 1, high)


if __name__ == '__main__':
    my_list = list(range(0, 10, 2))
    print(binary_search(my_list, 1))
