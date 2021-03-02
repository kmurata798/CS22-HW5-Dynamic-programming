class Memoize:
    def __init__(self, fn):
        self.fn = fn
        self.memo = {}

    def __call__(self, *args):
        if args not in self.memo:
            self.memo[args] = self.fn(*args)
        return self.memo[args]


@Memoize
def lcs(strA, strB):
    if len(strA) == 0 or len(strB) == 0:
        return 0
    elif strA[-1] == strB[-1]: # if the last characters match
        return 1 + lcs(strA[:-1], strB[:-1])
    else: # if the last characters don't match
        return max(lcs(strA[:-1], strB), lcs(strA, strB[:-1]))


def lcs_dp(strA, strB):
    """Determine the length of the Longest Common Subsequence of 2 strings."""
    rows = len(strA) + 1
    cols = len(strB) + 1

    #           array of arrays with 0's
    dp_table = [[0 for j in range(cols)] for i in range(rows)]

    # Fill in the table using a nested for loop.
    for row in range(1, rows):
        for col in range(1, cols):
            # if strA[row - 1] == strB[col - 1]:
            #     dp_table[row][col] = dp_table[row - 1][col - 1] + 1
            # else:
            #     dp_table[row][col] = max(dp_table[row][col - 1], dp_table[row - 1][col])
            
            # REFACTORED VERSION (IF/ELSE statement One-liner) 
            dp_table[row][col] = (dp_table[row - 1][col - 1] + 1
                                 if strA[row - 1] == strB[col - 1]
                                 else max(dp_table[row][col - 1],
                                          dp_table[row - 1][col]))

    return dp_table[rows-1][cols-1]

def knapsack(items, capacity):
    """Return the maximum value that can be stored in the knapsack using the
    items given."""
    # Go through every possible choice of adding values and skipping values based
    # on the capacity of the knapsack to find the highest outcome.
    # BASE CASE: If items == [], or capacity == 0, then return 0
    if len(items) == 0 or capacity <= 0:
        return 0
    first_value = items[0][2]
    first_weight = items[0][1]
    other_items = items[1:]

    # Take the value of the first item, add it to whatever the value
    # of the remaining items would be, but subtract capacity by the 
    # first item's weight
    value_with = first_value + knapsack(other_items, capacity - first_weight)
    
    # The total value assuming the first item doesn't go in the knapsack
    value_without = knapsack(other_items, capacity)
    
    # Check to see if the total weight exceeds the capacity
    if capacity - first_weight < 0:
        return value_without
    else:
        return max(value_with, value_without)

def knapsack_dp(items, capacity):
    """Return the maximum value that can be stored in the knapsack using the
    items given."""
    rows = len(items) + 1
    cols = capacity + 1
    dp_table = [[0 for j in range(cols)] for i in range(rows)]

    # Fill in the table using a nested for loop.
    # Loop through the table
    for row in range(rows):
        for col in range(cols):
            # # If it's over capacity then grab the previous value
            # if items[row-1][1] > col:
            #     dp_table[row][col] = dp_table[row-1][col]
            # else:
            #     value_with = items[row-1][2] + dp_table[row-1][col - items[row-1][1]]
            #     value_without = dp_table[row-1][col]
            # # Compare which value is greater since the capacity hasn't been reached
            #     dp_table[row][col] = max(value_with, value_without)
            
            # REFACTORED VERSION (IF/ELSE statement One-liner)
            dp_table[row][col] = (dp_table[row - 1][col]
                                  if items[row - 1][1] > col
                                  else max(items[row - 1][2] + dp_table[row - 1][col - items[row - 1][1]],
                                           dp_table[row - 1][col]))
    return dp_table[rows-1][cols-1]

@Memoize
def edit_distance(str1, str2):
    """Compute the Edit Distance between 2 strings."""
    # BASE CASE 1:
    # If one of the strings is empty,tThe solution will be the length of the other non-empty string
    if len(str1) == 0 or len(str2) == 0:
        return max(len(str1), len(str2))
    
    # BASE CASE 2:
    # Check if the last letters are equal
    if str1[-1] == str2[-1]:
        # If the last letters are equal, then run function again without the last letter from each string
        return edit_distance(str1[:-1], str2[:-1])

    # Compare the 3 possible options and grab the smallest value and then adding + 1 to it
    insert = edit_distance(str1[:-1], str2)
    delete = edit_distance(str1, str2[:-1])
    replace = edit_distance(str1[:-1], str2[:-1])

    return 1 + min(insert, delete, replace)

def edit_distance_dp(str1, str2):
    """Compute the Edit Distance between 2 strings."""
    rows = len(str1) + 1
    cols = len(str2) + 1
    dp_table = [[0 for j in range(cols)] for i in range(rows)]

    # Fill in the table using a nested for loop.
    for row in range(1, rows):
        for col in range(1, cols):
            insert = dp_table[row - 1][col]
            delete = dp_table[row][col - 1]
            replace = dp_table[row - 1][col - 1]
            # if str1[row - 1] == str2[col - 1]:
            #     dp_table[row][col] = replace 
            # else:
            #     dp_table[row][col] = min(insert, delete) + 1

            # REFACTORED VERSION (IF/ELSE statement One-liner)
            dp_table[row][col] = (replace 
                                  if str1[row - 1] == str2[col - 1]
                                  else 1 + min(insert, delete))

    return dp_table[rows-1][cols-1]
