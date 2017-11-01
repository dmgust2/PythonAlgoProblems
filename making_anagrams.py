# HackerRank CCI:
# https://www.hackerrank.com/challenges/ctci-making-anagrams/problem
# Python 3


# -----------------------------------------------------------------------------
# Number of chars required to delete from each passed string a, b to get anagrams
# Constraints:
# 1 <= |a|, |b| <= 10000 (10^4)
# It is guaranteed that strings a and b consist of lowercase English alphabetic letters (i.e. a-z).
def number_needed(first, second):
    number_of_deletions = 0
    # Create hash/dict that maps chars a-z to their count
    letters = {}

    # First iterate over the first string and update frequency of letters found (increment)
    for char in first:
        if char in letters:
            letters[char] += 1
        else:
            letters[char] = 1

    # Now iterate over the second string and update the frequency of letters found (decrement)
    for char in second:
        if char in letters:
            letters[char] -= 1
        else:
            letters[char] = -1

    # Now sum the char frequencies in the letters array using ABS
    for char in letters:
        number_of_deletions += abs(letters[char])

    return number_of_deletions


# **NOTE: This passed most tests, but not efficient enough (don't need to get the actual strings anagrams)
def old_number_needed(a, b):
    # First remove any chars in a not in b, or extra occurrences in a
    new_string_a = remove_chars(a, b)
    # DEBUG
    print('NEW modified string A: ', new_string_a)
    # Total char deletions is original string a - new_string_a length
    total_deletions = len(a) - len(new_string_a)

    # Now remove any chars in b not in the new string a from above, or extra occurrences in b
    new_string_b = remove_chars(b, new_string_a)
    # DEBUG
    print('NEW modified string B: ', new_string_b)
    # Total char deletions is total deletions from above + original string_b - new_string_b length
    total_deletions += len(b) - len(new_string_b)

    return total_deletions


# -----------------------------------------------------------------------------
# Removes chars from string_one NOT found in string_two recursively
# **NOTE: This passed most tests, but not efficient enough (don't need to get the actual strings anagrams)
def remove_chars(string_one, string_two):
    new_string = None

    # Remove any chars in string_a not in string_b
    for char in string_one:
        # DEBUG
        print('String ONE: ', string_one)
        print('Char: ', char)

        # If char is not in string_two, remove any occurrences from string_one
        if char not in string_two:
            # Remove ALL occurrences of this char
            new_string = string_one.replace(char, '')
            # DEBUG
            print('Removed ALL occurrences of char: ', char)
            new_string = remove_chars(new_string, string_two)
            break
        # Else check the strings have the same number of occurrences of this char
        else:
            if string_one.count(char) > string_two.count(char):
                # Just remove ONE occurrence of this char
                new_string = string_one.replace(char, '', 1)
                # DEBUG
                print('Removed ONE occurrence of char: ', char)
                new_string = remove_chars(new_string, string_two)
                break

    new_string = string_one if new_string is None else new_string
    # DEBUG
    print('Returning NEW string: ', new_string)
    return new_string


# -----------------------------------------------------------------------------
# Main
# -----------------------------------------------------------------------------

# User Input
# a = input().strip()
# b = input().strip()

# Tests
#a = 'cde'
#b = 'abc'

# a = 2; b = 1; c = 2; d = 2; e = 1; f = 1; g = 1 ... z = 0
# a = 2; b = 1; c = 1; d = 1; e = 1; f = 1; g = -2 ... z = 2
# Total => 11
a = 'abccddefag'
b = 'cdgggzz'

print(number_needed(a, b))
