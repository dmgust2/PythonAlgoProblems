#
# Given 2 arrays (sorted and distinct), find the * elements in common
#   Example: A = [1, 5, 15, 20, 30, 37]
#            B = [2, 5, 13, 30, 32, 35, 37, 42]
#   Elements in common -> [5, 30, 37]


# -----------------------------------------------------------------------------
# Compute common elements in two arrays
def compute_common_numbers(first, second):
    # TODO: Since they are sorted, iterate over the shortest one first?
    # Build the common numbers array list
    c = []
    for number in first:
        if number in second:
            c.append(number)

    return c


# -----------------------------------------------------------------------------
# Main
# -----------------------------------------------------------------------------
# a = [2, 5]
# b = [2]
a = [1, 5, 15, 20, 30, 37]
b = [2, 5, 13, 30, 32, 35, 37, 42]

common_numbers = compute_common_numbers(a, b)

# Print common numbers array
print(*common_numbers, sep=' ')
