#!python


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
    counter = 0
    counter_mod = 1
    swapped = False
    while not sortd:
      if counter < len(items) - counter_mod:
        item = items[counter]
        adj = items[counter + 1]

        if item > adj:
          swapped = True
          items[counter] = adj
          items[counter + 1] = item
          if counter + 1 == len(items) - counter_mod:
            counter_mod += 1
        
        counter += 1
      else:
        if not swapped:
          sortd = True
        
        counter = 0
        swapped = False



def selection_sort(items):
    """Sort given items by finding minimum item, swapping it with first
    unsorted item, and repeating until all items are in sorted order.
    TODO: Running time: ??? Why and under what conditions?
    TODO: Memory usage: ??? Why and under what conditions?"""
    # TODO: Repeat until all items are in sorted order
    # TODO: Find minimum item in unsorted items
    # TODO: Swap it with first unsorted item


def insertion_sort(items):
    """Sort given items by taking first unsorted item, inserting it in sorted
    order in front of items, and repeating until all items are in order.
    TODO: Running time: ??? Why and under what conditions?
    TODO: Memory usage: ??? Why and under what conditions?"""
    # TODO: Repeat until all items are in sorted order
    # TODO: Take first unsorted item
    # TODO: Insert it in sorted order in front of items


# if __name__ == '__main__':
#   l = [10, 420, 20, 10, 600, 1, 1, 430, 520, 102, 320, 21, 415, 4]
#   print(l)
#   bubble_sort(l)
#   print(l)
