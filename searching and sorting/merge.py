# ---------------------------------------
# Merge Sort
# ---------------------------------------

'''
Merge Sort

Technique:
Divide and Conquer

Idea:
1. Divide the array into two halves.
2. Recursively sort both halves.
3. Merge the two sorted halves.

Process:
Divide → Sort → Merge

Time Complexity:
O(n log n)

Space Complexity:
O(n) (extra arrays used for merging)
'''

# ---------------------------------------
# Divide Function
# ---------------------------------------
# Recursively splits the array into halves
# until only one element remains

def divide(arr, l, r):

    if l < r:

        # find middle index
        m = (l + r) // 2

        # recursively divide left half
        divide(arr, l, m)

        # recursively divide right half
        divide(arr, m + 1, r)

        # merge the two sorted halves
        merge(arr, l, m, r)


# ---------------------------------------
# Merge Function
# ---------------------------------------
# Combines two sorted subarrays into one

def merge(arr, l, m, r):

    # size of left and right subarrays
    s1 = m - l + 1
    s2 = r - m

    # temporary arrays
    L = [0] * s1
    R = [0] * s2

    # copy data into temporary arrays
    for i in range(s1):
        L[i] = arr[l + i]

    for j in range(s2):
        R[j] = arr[m + 1 + j]

    # initial indexes
    i = 0
    j = 0
    k = l

    # merge the two arrays
    while i < s1 and j < s2:

        if L[i] <= R[j]:

            arr[k] = L[i]
            i += 1

        else:

            arr[k] = R[j]
            j += 1

        k += 1

    # copy remaining elements of L[]
    while i < s1:
        arr[k] = L[i]
        i += 1
        k += 1

    # copy remaining elements of R[]
    while j < s2:
        arr[k] = R[j]
        j += 1
        k += 1


# ---------------------------------------
# Driver Code
# ---------------------------------------

arr = [7, 8, 0, 5, 6, 4, 3]

divide(arr, 0, len(arr) - 1)

print(arr)