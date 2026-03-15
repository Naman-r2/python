# ---------------------------------------
# Dynamic Programming (DP) - 0/1 Knapsack
# ---------------------------------------

"""
Dynamic Programming (DP)
========================

Dynamic Programming is a technique used to solve problems that have:

1. Overlapping Subproblems
   The same smaller problem is solved multiple times.

2. Optimal Substructure
   The optimal solution of the main problem can be built
   using optimal solutions of smaller subproblems.

Instead of recomputing the same work repeatedly,
we STORE results and reuse them.

Two common DP approaches:

1. Memoization (Top-Down)
   Recursion + caching results.

2. Tabulation (Bottom-Up)
   Build a table from smallest subproblem → largest problem.

---------------------------------------
Problem: 0/1 Knapsack
---------------------------------------

We are given:
- weights of items
- values of items
- capacity of the knapsack

Goal:
Maximize total value without exceeding capacity.

Constraint:
Each item can be taken ONLY ONCE (0 or 1).

---------------------------------------
Example
---------------------------------------

weights = [2,3,4,5]
values  = [3,4,5,6]
capacity = 5

Possible combinations:

item0 -> weight 2 value 3
item1 -> weight 3 value 4
item2 -> weight 4 value 5
item3 -> weight 5 value 6

Best combination:
item0 + item1
weight = 5
value = 7

So answer = 7
"""

# ---------------------------------------------------
# Recursive version (Top-Down idea)
# ---------------------------------------------------
# This version shows the conceptual logic,
# but it recomputes many subproblems.

# def knapsack_recursive(weights, values, capacity, n):
#
#     # Base case
#     # If no items left or capacity is 0
#     if n == 0 or capacity == 0:
#         return 0
#
#     # If weight of last item exceeds capacity
#     # we cannot include it
#     if weights[n - 1] > capacity:
#         return knapsack_recursive(weights, values, capacity, n - 1)
#
#     # Choice 1: Include item
#     include = values[n - 1] + knapsack_recursive(
#         weights,
#         values,
#         capacity - weights[n - 1],
#         n - 1
#     )
#
#     # Choice 2: Exclude item
#     exclude = knapsack_recursive(weights, values, capacity, n - 1)
#
#     # Return best option
#     return max(include, exclude)


# ---------------------------------------------------
# Dynamic Programming (Tabulation / Bottom-Up)
# ---------------------------------------------------

def knapsackDP(wt, value, capacity):

    # Number of items
    n = len(wt)

    """
    DP Table Creation
    -----------------

    dp[i][w] represents:

    Maximum value achievable
    using first i items
    with capacity w.

    Dimensions:
    (n+1) rows  -> items considered
    (capacity+1) columns -> possible capacities

    Why +1 ?

    Row 0 -> no items
    Column 0 -> capacity 0

    These are base cases.
    """

    dp = [[0] * (capacity + 1) for _ in range(n + 1)]

    """
    Initial table looks like:

        capacity →
        0 1 2 3 4 5

    i
    0   0 0 0 0 0 0
    1   0
    2   0
    3   0
    4   0

    Row 0 = no items → value = 0
    Column 0 = capacity 0 → value = 0
    """

    # ---------------------------------------------------
    # Fill DP table
    # ---------------------------------------------------

    for i in range(1, n + 1):

        """
        i represents how many items we are considering.

        i = 1 -> first item
        i = 2 -> first two items
        i = 3 -> first three items
        """

        for w in range(1, capacity + 1):

            """
            w represents current capacity we are testing.
            """

            # If current item's weight fits in capacity
            if wt[i - 1] <= w:

                """
                We have two choices:

                1. EXCLUDE the item
                   value = dp[i-1][w]

                2. INCLUDE the item
                   value = value[i-1] + dp[i-1][w - wt[i-1]]

                Why w - wt[i-1] ?

                Because if we include the item,
                we reduce the remaining capacity.
                """

                dp[i][w] = max(
                    dp[i - 1][w],                     # exclude item
                    dp[i - 1][w - wt[i - 1]] + value[i - 1]  # include item
                )

            else:

                """
                If item weight exceeds capacity,
                we cannot include it.
                So we simply copy previous result.
                """

                dp[i][w] = dp[i - 1][w]

    """
    After filling the table,
    the answer will be in:

    dp[n][capacity]

    Because:
    - n items considered
    - full capacity available
    """

    print("Max profit is", dp[n][capacity])


# ---------------------------------------------------
# Driver Code
# ---------------------------------------------------

weights = [2, 3, 4, 5]
values = [3, 4, 5, 6]

knapsackDP(weights, values, 5)