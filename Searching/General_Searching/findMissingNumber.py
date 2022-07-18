"""
Finding the Missing Number: We are given a list of n-1
integers and these integers are in the range of 1 to . There
are no duplicates in the list. One of the integers is missing
in the list. Given an algorithm to find the missing integer.
"""

"""
Alternative problem statement: There is an array of numbers.
A second array is formed by shuffling the elements of the
first array and deleting a random element. Given these
two arrays, find which element is missing in the second
array.
"""


import collections
A = [1, 2, 4, 6, 3, 7, 8]


def findMissingNumber(A):
    n = len(A)
    for i in range(1, n+1):
        if i in A:
            continue
        else:
            return i
    return "No missing"


def findMissingNumber(A):
    n = len(A)
    for i in range(1, n+1):
        found = False
        for j in A:
            if i == j:
                found = True
        if not found:
            print(f'Missing number is {i}')
            return
    return


B = [8, 2, 1, 4, 6, 5, 7, 9]
# findMissingNumber(B)


def findMissingNumberSort(A):
    A.sort()
    for i in range(len(A)-1):
        if A[i] + 1 != A[i+1]:
            print("Missing number is, ", A[i] + 1)


def findMissingNumberHash(A):
    table = {}
    n = len(A) + 2
    for i in A:
        if i != "":
            table[i] = 1
        else:
            table[i] = 0

    for i in range(1, n):
        if i in table:
            table[i] += 1
        else:
            table[i] = 1

    for x in range(1, n):
        count = table[x]
        print(count)
        if count == 1:
            return f'Missing number is {x}'


def findMissingNumberHash2(A):
    d = collections.defaultdict(int)
    n = len(A)
    for num in A:
        d[num] += 1
    print(d)
    for num in range(1, n+2):
        if d[num] == 0:
            return num
        else:
            d[num] -= 1


x = findMissingNumberHash2(B)
print(x)
# n = len(B) + 2
# for num in range(1, n):
#     print(num)
