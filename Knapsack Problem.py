
# The knapsack problem is given a collection of items with weights and values, we want to fill a knapsack
# with a specific capacity so that the value of the items we have are maximised.

# params:
# items = length n list, each entry is a list, (weight, value).
# c = maximum capacity of the knapsack
def knapsack(items, c):
    if c <= 0:
        return 0
    elif len(items) == 1 and items[0][0] > c:
        return 0
    elif len(items) == 1 and items[0][0] <= c:
        return items[0][1]
    else:
        return max(knapsack(items[:-1], c-items[-1][0]) + items[-1][1], knapsack(items[:-1], c))


