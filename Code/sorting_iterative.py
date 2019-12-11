#!python
from binaryheap import BinaryMinHeap


def is_sorted(items):
    """Return a boolean indicating whether given items are in sorted order.
    TODO: Running time: O(n) n = length of items. Since it has to run through the list
    TODO: Memory usage: O(1) it doesn't create any new variables except for keeping track of the previous item"""
    prev = None
    for item in items:
      if prev != None and item < prev:
        return False
      prev = item
    return True



def bubble_sort(items):
    """Sort given items by swapping adjacent items that are out of order, and
    repeating until all items are in sorted order.
    TODO: Running time: O(n^2) since if all items are out of order, it will have to perform n operations on n items
    TODO: Memory usage: O(1) since it only manipulates the input variable without creating a new list"""

    sortd = False
    index = 0
    index_mod = 1
    swapped = False
    while not sortd:
      if index < len(items) - index_mod:
        item = items[index]
        adj = items[index + 1]

        if item > adj:
          swapped = True
          items[index] = adj
          items[index + 1] = item
          if index + 1 == len(items) - index_mod:
            index_mod += 1
        
        index += 1
      else:
        if not swapped:
          sortd = True
        
        index = 0
        swapped = False



def selection_sort(items):
    """Sort given items by finding minimum item, swapping it with first
    unsorted item, and repeating until all items are in sorted order.
    TODO: Running time: O(logn * n) since it has to do logn operations on n tiems
    TODO: Memory usage: O(1) it only manipulates the input list"""

    sortd = len(items) < 1
    already_sorted = 0
    while not sortd:
      min_val_index = None
      for index in range(already_sorted, len(items)):
        if min_val_index == None or items[index] < items[min_val_index]:
          min_val_index = index
      first_unsorted = items[already_sorted]
      item_to_swap = items[min_val_index]

      items[min_val_index] = first_unsorted
      items[already_sorted] = item_to_swap

      already_sorted += 1

      if already_sorted == len(items):
        sortd = True

def heap_sort(items):
  heap = BinaryMinHeap(items)

  sorted_items = []

  while heap.size() > 0:
    sorted_items.append(heap.delete_min())

  items[:] = sorted_items



def insertion_sort(items):
    """Sort given items by taking first unsorted item, inserting it in sorted
    order in front of items, and repeating until all items are in order.
    TODO: Running time: O(logn * n) since it has to do logn operations on n tiems
    TODO: Memory usage: O(1) it only manipulates the input list"""

    already_sorted = 0
    for i in range(len(items)):
      item = items[i]
      for j in range(already_sorted - 1, -1, -1):
        if items[j] > item:
          items[j+1] = items[j]
          items[j] = item
        else:
          break
      already_sorted += 1


# if __name__ == '__main__':
#   l = [10, 420, 20, 10, 600, 1, 1, 430, 520, 102, 320, 21, 415, 4]
#   print(l)
#   # bubble_sort(l)
#   # selection_sort(l)
#   insertion_sort(l)
#   print(l)
