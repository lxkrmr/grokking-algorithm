import random


def quicksort(arr):
    if len(arr) < 2:
        return arr

    pivot = random.choice(arr)
    copy = list(arr)
    copy.remove(pivot)

    less = [x for x in copy if x <= pivot]
    greater = [x for x in copy if x > pivot]

    return quicksort(less) + [pivot] + quicksort(greater)


if __name__ == '__main__':
    print(quicksort([]))
    print(quicksort([1]))
    print(quicksort([2, 1]))
    print(quicksort([3, 2, 1]))
    print(quicksort([88, 0, 14, 5, 72, 4, 122, 101345, 45, 78, 99, 1234, 234, 45678, 1]))
