# HackerRank CCI:
# https://www.hackerrank.com/challenges/ctci-is-binary-search-tree?h_r=next-challenge&h_v=zen
# Python 3


# -----------------------------------------------------------------------------
# Node is defined as
# -----------------------------------------------------------------------------
class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None


# Creates a BST (if passed a sorted array of ints)
# -----------------------------------------------------------------------------
def create_balanced_tree(sorted_int_array):
    if not sorted_int_array:
        return None

    # DEBUG
    # print('Currently creating BST with:', *sorted_int_array, sep=' ')

    # First find the middle element to create the correct root node (uses floor div)
    mid = len(sorted_int_array) // 2
    root = Node(sorted_int_array[mid])

    # Python slice notation:
    # a[start:end]  # items start through end-1
    # a[start:]     # items start through the rest of the array
    # a[:end]       # items from the beginning through end-1
    # a[:]          # a copy of the whole array

    # Recursively create the BST children nodes
    # Pass array items start -> (mid - 1)
    root.left = create_balanced_tree(sorted_int_array[:mid])
    # Pass array items (mid + 1) -> end
    root.right = create_balanced_tree(sorted_int_array[mid + 1:])

    return root


# To check if the passed tree is a BST:
# The data value of every node in a node's left subtree is less than the data value of that node.
# The data value of every node in a node's right subtree is greater than the data value of that node.
# Note: We do not consider a binary tree to be a binary search tree if it contains duplicate values.
# return boolean
# -----------------------------------------------------------------------------
def checkBST(root):
    # The MAX allowed tree data integer value is 10^4 = 10000
    max_integer = 10000
    return check_binary_search_tree(root, 0, max_integer)


# Overloading is not supported in Python
def check_binary_search_tree(tree_node, min_int, max_int):
    if tree_node is None:
        return True

    # Can simplify from this: min < tree_node.data and tree_node.data < max
    return min_int < tree_node.data < max_int and \
           check_binary_search_tree(tree_node.left, min_int, tree_node.data) and \
           check_binary_search_tree(tree_node.right, tree_node.data, max_int)


# -----------------------------------------------------------------------------
# To print we need to implement a BFS algo to traverse
def print_binary_search_tree(tree_root):
    # DEBUG
    print('Printing BST:')

    current_level = [tree_root]
    while current_level:
        next_level = list()
        for n in current_level:
            print(n.data)
            if n.left:
                next_level.append(n.left)
            if n.right:
                next_level.append(n.right)
        print('------')
        current_level = next_level


# -----------------------------------------------------------------------------
# Main
# -----------------------------------------------------------------------------

# Create a simple node tree for testing
#                  3
#                /   \
#               2     6
# tree_root = create_balanced_tree([2, 3, 6])
#                  4
#                /   \
#               2     6
#             /   |  |  \
#            1    3  5   7
# tree_root = create_balanced_tree([1, 2, 3, 4, 5, 6, 7])
# tree_root = create_balanced_tree([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31])
tree_root = create_balanced_tree([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 17, 16, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31])

# DEBUG
print_binary_search_tree(tree_root)

# Check if the passed node is a BST
answer_bool = checkBST(tree_root)

# Ternary operator
answer = 'Yes' if answer_bool is True else 'No'

print(answer)
