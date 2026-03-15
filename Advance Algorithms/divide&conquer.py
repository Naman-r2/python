# ---------------------------------------
# Divide and Conquer : Find Min and Max
# ---------------------------------------

'''
Problem:
Find the minimum and maximum element in an array
using Divide and Conquer.

Idea:
1. Divide the array into two halves.
2. Recursively find min and max in both halves.
3. Compare results to get final min and max.

Advantages:
Uses fewer comparisons than the naive approach.

Time Complexity:
O(n)

Comparisons:
~ 3n/2 comparisons (better than 2n in naive method)
'''

def find_min_max(arr, start, end):

    # ---------------------------------------
    # Base Case 1: Only one element
    # ---------------------------------------
    if start == end:
        return arr[start], arr[start]

    # ---------------------------------------
    # Base Case 2: Two elements
    # ---------------------------------------
    if start + 1 == end:

        if arr[start] < arr[end]:
            return arr[start], arr[end]
        else:
            return arr[end], arr[start]

    # ---------------------------------------
    # Divide Step
    # ---------------------------------------
    mid = (start + end) // 2

    # find min and max in left half
    min1, max1 = find_min_max(arr, start, mid)

    # find min and max in right half
    min2, max2 = find_min_max(arr, mid + 1, end)

    # ---------------------------------------
    # Combine Step
    # ---------------------------------------
    return min(min1, min2), max(max1, max2)


# ---------------------------------------
# Driver Code
# ---------------------------------------

arr = [23, 43, 3, 4, 6, 10]

print(find_min_max(arr, 0, len(arr) - 1))