# HackerRank CCI:
# https://www.hackerrank.com/challenges/ctci-array-left-rotation/problem
# Python 3


# -----------------------------------------------------------------------------
def array_left_rotation(a, n, k):
    b = []
    i = 0

    # I believe this is basically O(n)
    for val in a:
        idx = (i + (n - k)) % n
        b.insert(idx, val)
        i += 1

    return b


# -----------------------------------------------------------------------------
# Main
# -----------------------------------------------------------------------------
n, k = map(int, input().strip().split(' '))
a = list(map(int, input().strip().split(' ')))
answer = array_left_rotation(a, n, k)
print(*answer, sep=' ')
