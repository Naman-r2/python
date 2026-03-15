# ---------------------------------------
# Quick Sort
# ---------------------------------------

'''
Quick Sort

Technique:
Divide and Conquer

Idea:
1. Choose a pivot element.
2. Rearrange the array so:
   - elements smaller than pivot go to the left
   - elements larger than pivot go to the right
3. Place pivot in its correct position.
4. Recursively sort left and right parts.

Important Terms:
pivot -> element used for partitioning

Average Time Complexity -> O(n log n)
Worst Case -> O(n^2) (when pivot selection is bad)

Space Complexity -> O(log n) recursion stack
'''

# ---------------------------------------
# QuickSort Function
# ---------------------------------------
# Recursively sorts left and right partitions

def QuickSort(arr, l, r):

    # base condition
    if l < r:

        # find correct position of pivot
        p = partition(arr, l, r)

        # sort left part
        QuickSort(arr, l, p - 1)

        # sort right part
        QuickSort(arr, p + 1, r)


# ---------------------------------------
# Partition Function
# ---------------------------------------
# Places pivot element in correct position
# and arranges smaller elements on left
# and larger elements on right

def partition(arr, l, r):

    pivot = arr[l]      # choose first element as pivot

    i = l + 1           # pointer from left
    j = r               # pointer from right

    while True:

        # move i right while elements < pivot
        while i <= j and arr[i] <= pivot:
            i = i + 1

        # move j left while elements > pivot
        while i <= j and arr[j] > pivot:
            j = j - 1

        # swap if pointers have not crossed
        if i < j:
            arr[i], arr[j] = arr[j], arr[i]

        else:
            break

    # place pivot at correct position
    arr[j], arr[l] = arr[l], arr[j]

    return j


# ---------------------------------------
# Driver Code
# ---------------------------------------

arr = [23, 45, 12, 65, 34, 10, 3]

QuickSort(arr, 0, len(arr) - 1)

print(arr)