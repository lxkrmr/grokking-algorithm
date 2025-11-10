def my_sum(arr):
    # return my_sum_rec(arr) --> can not even process arr with 1_000 entries
    # return my_sum_loop(arr)
    return sum(arr)


def my_sum_rec(arr, index=0, total=0):
    if len(arr) == 0:
        return 0
    if len(arr) == index:
        return total

    total += arr[index]
    index += 1

    return my_sum_rec(arr, index, total)


def my_sum_loop(arr):
    total = 0
    for x in arr:
        total += x
    return total


if __name__ == '__main__':
    my_list = range(1_000_000_000)  # 210
    print(my_sum(my_list))
