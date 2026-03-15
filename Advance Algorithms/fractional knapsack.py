# ---------------------------------------
# Fractional Knapsack (Greedy)
# ---------------------------------------

'''
Problem:
We are given:
- n items
- each item has weight and value
- a knapsack with capacity W

Goal:
Maximize the total value inside the knapsack.

Important:
Unlike 0/1 knapsack, here we CAN take fractions of an item.

Greedy Strategy:
Choose items based on the highest value/weight ratio.

Steps:
1. Compute value/weight ratio for each item.
2. Sort items in descending order of ratio.
3. Pick items until capacity is full.
4. If an item doesn't fit completely, take the fraction that fits.

Time Complexity:
O(n log n) (sorting step)
'''

def fractional_knapsack(item_wt, price, capacity):

    n = len(item_wt)

    # ---------------------------------------
    # Create a list of items:
    # (value, weight, value/weight ratio)
    # ---------------------------------------
    items = [(price[i], item_wt[i], price[i] / item_wt[i]) for i in range(n)]

    # ---------------------------------------
    # Sort items by value/weight ratio
    # (descending order)
    # ---------------------------------------
    items.sort(key=lambda x: x[2], reverse=True)

    profit = 0.0

    # ---------------------------------------
    # Pick items greedily
    # ---------------------------------------
    for value, weight, ratio in items:

        # if whole item can fit
        if capacity >= weight:

            capacity -= weight
            profit += value

        # if only fraction can fit
        else:

            profit += ratio * capacity
            capacity = 0
            break   # knapsack full

    print("Total profit =", profit)


# ---------------------------------------
# Driver Code
# ---------------------------------------

price = [24, 21, 12, 10]
items_wt = [7, 3, 4, 5]
capacity = 20

fractional_knapsack(items_wt, price, capacity)