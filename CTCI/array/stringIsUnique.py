from collections import Counter
x = "majid"

def isUnique(x):
    table = {}
    for s in x:
        if s in table:
            print("Not Unique")
            return False
        elif s != " ":
            table[s] = 1
        else:
            table[s] = 0
    print(table)

def all_uniqs(input_str: str):
    ctr = Counter(input_str)

    for k, v in ctr.items():
        if v > 1:
            return False
    return True

def all_uniqs_no_datastruct(x: str):
    sorted_x = sorted(x)
    n = len(x)
    for i in range(1, n):
        if sorted_x[i-1] == sorted_x[i]:
            return False
    return True

def isUniqueWithAscii(string):
    if len(string) > 128:
        return False

    chars_list = [False] * 128
    for char in string:
        if chars_list[ord(char)]:
            return False
        chars_list[ord(char)] = True
    return True
    #  if no ASCII alphabets is only 128-character


def is_unique_chars_compare(string):
    """
    This solution compares every character of string to 
    every other character of string.

        Time Complexity: O(n^2)
        Space Complexity: O(1)
    """

    for i, char in enumerate(string):
        for j, other_chars in enumerate(string):
            if i != j and char == other_chars:
                return False
    return True
