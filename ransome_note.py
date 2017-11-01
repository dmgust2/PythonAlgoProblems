#
# HackerRank CCI:
# https://www.hackerrank.com/challenges/ctci-ransom-note/problem
# @author Gusto
#


# -----------------------------------------------------------------------------
# Populate hashmaps/dict from the user input strings
# Return True if can build the ransom note, False if you cannot
def ransom_note(mag_array, note_array):
    # First build/populate the magazine dictionary (key:word, value:count)
    mag_dict = {}
    for word in mag_array:
        if word in mag_dict:
            mag_dict[word] += 1
        else:
            mag_dict[word] = 1

    # Now build/populate the ransome note dictionary (key:word, value:count)
    note_dict = {}
    for word in note_array:
        if word in note_dict:
            note_dict[word] += 1
        else:
            note_dict[word] = 1

    # Debug
    print_dicts(mag_dict, note_dict)

    # Now determine (solve) whether you can construct the ransome note from the magazine
    return solve(mag_dict, note_dict)


# -----------------------------------------------------------------------------
# All words in the ransom note (including frequency of words) must be in the magazine to build the ransom note
# Return True if can build the ransom note, False if you cannot
def solve(mag_dict, note_dict):
    for word in note_dict:
        if word in mag_dict:
            if note_dict[word] > mag_dict[word]:
                return False
        else:
            return False

    return True


# -----------------------------------------------------------------------------
# For DEBUG, print out the dictionaries
def print_dicts(mag_dict, note_dict):
    print("\nMagazine:")
    for word in mag_dict:
        print(word, ': ', mag_dict[word])

    print("\nRansom Note:")
    for word in note_dict:
        print(word, ': ', note_dict[word])


# -----------------------------------------------------------------------------
# Main
# -----------------------------------------------------------------------------
# Read in user input, create array of strings (words)
m, n = map(int, input().strip().split(' '))
magazine = input().strip().split(' ')
ransom = input().strip().split(' ')

# If there are more words in the note than in the magazine, you can't build it
if n > m:
    print("\nNo")
else:
    answer = ransom_note(magazine, ransom)
    if answer:
        print("\nYes")
    else:
        print("\nNo")
