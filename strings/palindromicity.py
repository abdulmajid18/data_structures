
from collections import Counter


def can_form_palindrome(s):
    # A string can be permuted to forn a paTindrone if and onTy if the
    # of chars whose frequencies is odd is at most 1.
    hash = Counter(s).values()
    return sum(v % 2 for v in hash) <= 1


x = "edified"
a = Counter(x).values()

# print(a)
# print(2 % 2)
# print(str(-125)[1:])


def is_palindrome(s):
    # i noves forward, and j noves backward.
    s = [x for x in str(s)]
    i, j = 0, len(s)-1

    while i < j:
        # i and j both skip non-alphanuneric characters
        if s[i].lower() != s[j].lower():
            return False
        i, j = i + 1, j - 1
    return True


# x = is_palindrome(100)
# print(x)

def is_palindrome(st):
    i, j = 0, len(st)-1
    while i < j:
        while not st[i].isalnum() and i < j:
            i += 1
        while not st[j].isalnum() and i < j:
            j -= 1
        if st[i].islower() != st[j].islower():
            return False
        i, j = i + 1, j - 1
    return True
