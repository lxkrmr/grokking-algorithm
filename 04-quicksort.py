def my_max(arr, index=0, max_value=0):
    if index == len(arr):
        return max_value

    curr = arr[index]
    if curr > max_value:
        max_value = curr

    index += 1
    return my_max(arr, index, max_value)


if __name__ == '__main__':
    my_list = [20, 33, 2, 56, 12, 1, 0]
    print(my_max(my_list))
