#!python
from sorting_iterative import insertion_sort


def merge(items1, items2):
    """Merge given lists of items, each assumed to already be in sorted order,
    and return a new list containing all items in sorted order.
    TODO: Running time: ??? Why and under what conditions?
    TODO: Memory usage: ??? Why and under what conditions?"""
    # TODO: Repeat until one list is empty
    # TODO: Find minimum item in both lists and append it to new list
    # TODO: Append remaining items in non-empty list to new list

    items = list()

    counter1 = 0
    counter2 = 0

    list1 = items1 if items1 != None else list()
    list2 = items2 if items2 != None else list()

    while len(list1) + len(list2) > len(items):
        if counter1 == len(list1):
            items.append(list2[counter2])
            counter2 += 1
        elif counter2 == len(list2):
            items.append(list1[counter1])
            counter1 += 1
        elif items1[counter1] >= list2[counter2]:
            items.append(list2[counter2])
            counter2 += 1
        elif items2[counter2] > list1[counter1]:
            items.append(list1[counter1])
            counter1 += 1

    return items


def split_sort_merge(items):
    """Sort given items by splitting list into two approximately equal halves,
    sorting each with an iterative sorting algorithm, and merging results into
    a list in sorted order.
    TODO: Running time: ??? Why and under what conditions?
    TODO: Memory usage: ??? Why and under what conditions?"""
    # TODO: Split items list into approximately equal halves
    # TODO: Sort each half using any other sorting algorithm
    # TODO: Merge sorted halves into one list in sorted order

    middle = len(items) // 2

    array1 = items[:middle]
    array2 = items[middle:]

    insertion_sort(array1)
    insertion_sort(array2)

    return merge(array1, array2)


def merge_sort(items):
    """Sort given items by splitting list into two approximately equal halves,
    sorting each recursively, and merging results into a list in sorted order.
    TODO: Running time: ??? Why and under what conditions?
    TODO: Memory usage: ??? Why and under what conditions?"""
    # TODO: Check if list is so small it's already sorted (base case)
    # TODO: Split items list into approximately equal halves
    # TODO: Sort each half by recursively calling merge sort
    # TODO: Merge sorted halves into one list in sorted order

    if len(items) > 1:
        middle = len(items) // 2
        items1 = items[:middle]
        items2 = items[middle:]
        merge_sort(items1)
        merge_sort(items2)
        items[:] = merge(items1, items2)


def partition(items, low, high):
    """Return index `p` after in-place partitioning given items in range
    `[low...high]` by choosing a pivot (TODO: document your method here) from
    that range, moving pivot into index `p`, items less than pivot into range
    `[low...p-1]`, and items greater than pivot into range `[p+1...high]`.
    TODO: Running time: ??? Why and under what conditions?
    TODO: Memory usage: ??? Why and under what conditions?"""
    # TODO: Choose a pivot any way and document your method in docstring above
    # TODO: Loop through all items in range [low...high]
    # TODO: Move items less than pivot into front of range [low...p-1]
    # TODO: Move items greater than pivot into back of range [p+1...high]
    # TODO: Move pivot item into final position [p] and return index p

    pivot = items[low]

    left = low + 1
    right = high

    done = False
    while not done:
        while left <= right and items[left] <= pivot:
            left += 1
        while right >= left and items[right] >= pivot:
            right -= 1

        if right < left:
            done = True
        else:
            item_left = items[left]
            items[left] = items[right]
            items[right] = item_left

    item_low = items[low]
    items[low] = items[right]
    items[right] = item_low
    return right


def quick_sort(items, low=None, high=None):
    """Sort given items in place by partitioning items in range `[low...high]`
    around a pivot item and recursively sorting each remaining sublist range.
    TODO: Best case running time: ??? Why and under what conditions?
    TODO: Worst case running time: ??? Why and under what conditions?
    TODO: Memory usage: ??? Why and under what conditions?"""
    # TODO: Check if high and low range bounds have default values (not given)
    # TODO: Check if list or range is so small it's already sorted (base case)
    # TODO: Partition items in-place around a pivot and get index of pivot
    # TODO: Sort each sublist range by recursively calling quick sort

    if low == None:
        low = 0
    if high == None:
        high = len(items) - 1

    if low < high:
        pivot = partition(items, low, high)

        quick_sort(items, low, pivot - 1)
        quick_sort(items, pivot + 1, high)
