# ---------------------------------------
# Greedy Algorithm Example
# ---------------------------------------

'''
Greedy Algorithm

Idea:
At every step choose the locally optimal solution
hoping it leads to a global optimum.

Used when:
- future choices do not affect the optimality
- local best choice is safe

Examples:
Coin Change
Activity Selection
Huffman Coding
Minimum Spanning Tree
'''

'''
Problem:
You are given an array A of n elements.

Remove exactly n/2 elements from A and place them in array B.

Compute:
1. Maximum possible value of:
   sum(|A[i] - B[i]|)

2. Minimum possible value of:
   sum(|A[i] - B[i]|)

Greedy Observation:
Sort the array.

For MAX difference:
pair smallest elements with largest elements.

For MIN difference:
pair adjacent elements.
'''

def Max_min_diff(arr):

    # sort array
    arr.sort()

    n = len(arr)

    mid = n // 2

    max_diff = 0
    min_diff = 0

    j = n - 1

    # ---------------------------------------
    # Maximum difference
    # pair smallest with largest
    # ---------------------------------------
    for i in range(mid):

        max_diff += abs(arr[i] - arr[j])
        j -= 1

    # ---------------------------------------
    # Minimum difference
    # pair adjacent elements
    # ---------------------------------------
    for i in range(mid):

        min_diff += abs(arr[2*i] - arr[2*i + 1])

    print("Max diff =", max_diff)
    print("Min diff =", min_diff)


# ---------------------------------------
# Driver Code
# ---------------------------------------

arr = [12, 5, 25, 10, 2, 15, 8, 30]

Max_min_diff(arr)
