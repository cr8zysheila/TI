"""Implement quick sort in Python.
Input a list.
Output a sorted list."""
def quicksort(array):
    partition(array, 0, len(array) - 1)
    return array

def partition(a, start, end):
    if end <= start:
        return
    
    lo = start
    pivot = end
    
    while lo < pivot:
        if a[lo] > a[pivot]:
            a[lo], a[pivot - 1] = a[pivot - 1], a[lo]
            a[pivot - 1], a[pivot] = a[pivot], a[pivot - 1]
            pivot -= 1
        else:
            lo += 1
    print a
    print pivot
    partition(a, start, pivot - 1)
    partition(a, pivot + 1, end)
        

test = [21, 4, 1, 3, 9, 20, 25, 6, 21, 14]
print quicksort(test)
