from collections import Counter
# Solution - 1
def check_premutation_sort(string1, string2):
    """
    This solution sorts both string and checks 
    if two strings are equal or not after sorting.

    Time Complexity: O(n log(n))
    Space Complexity: O(n)
    """

    if len(string1) != len(string2):
        return False
    sorted_string1 = sorted(string1)
    sorted_string2 = sorted(string2)
    return sorted_string1 == sorted_string2


# Solution - 2
def check_permutation_list(string1, string2):
    """
    This solution uses an array to keep count of characters.
    First traverse through one string and count the characters,
    then traverse through second string to match counts of characters.

    Time Complexity: O(n)
    Space Complexity: O(n)
    """

    if len(string1) != len(string2):
        return False

    letters = [0] * 128
    for char in string1:
        letters[ord(char)] += 1

    for char in string2:
        letters[ord(char)] -= 1
        if letters[ord(char)] < 0:
            return False
    return True

def check_perm_ctr(a: str, b: str):
    ca = Counter(a)
    cb = Counter(b)

    for k, v in ca.items():
        if k not in cb:
            return False
        elif v != cb[k]:
            return False

    if any(k not in ca for k in cb):
        return False

    return True

def checkPermutation(s1, s2):
    if len(s1) != len(s2):
        return False

    count = {}
    for i in s1:
        count[i] = count.get(i, 0) + 1
    print(count)
    for i in s2:
        if i in count:
            count[i] -= 1
            if count[i] == 0:
                del count[i]
        else:
            return False
    return len(count) == 0
a = [1,2,5,3,7,0,7,3,5,2,1]
b = [7,3,1,2,5,0,5,2,1,3,7]
# ans = checkPermutation(a, b)
# print(ans)
# ans = check_premutation_sort(a,b)
# print(ans)
# x = Counter(a)
# y = Counter(b)
# print(x , y)
# print(x == y)
# table = {'odd':0,'even':0}
# for i in a:
#     if i % 2 == 1:
#         table['odd'] += 1
#     else:
#         table['even'] += 1
# ans = abs(table['even']-table['odd'])
# print(ans)