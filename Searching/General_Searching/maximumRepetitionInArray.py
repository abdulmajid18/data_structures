"""
Given an array of n numbers. 
Give an algorithm for finding the element 
which appears the maximum number of times in an array
"""


def maxRepetitionBruteForce(A):
    n = len(A)
    maxCount = 0
    count = 0
    element = 0
    for i in range(n):
        count = 1
        for j in range(i+1, n):
            if A[i] == A[j]:
                count += 1
        if count >= maxCount:
            maxCount = count
            element = A[i]
    return element, maxCount


def maxRepititionSort(A):
    A.sort()
    print(A)
    j = 0
    count = max = 1
    element = A[0]
    for i in range(1, len(A)):
        if A[i] == element:
            count += 1
            if count > max:
                max = count
                maxRepeatedElement = element
        else:
            count = 1
            element = A[i]

    print(maxRepeatedElement)


def maxRepitionWithHash(A):
    table = {}
    for element in A:
        if element in table:
            table[element] += 1
        elif element != "":
            table[element] = 1
        else:
            table[element] = 0
    max = 0
    for i in A:
        count = table[i]
        if count >= max:
            max = count
            maxElement = i
    print(maxElement)


def maxRepititionEfficient(A):
    n = len(A)
    max = 0
    for i in range(0, len(A)):
        A[A[i] % n] += n
    print(A)
    # his solution is incomplete source Narasmha pytho page 285


A = [3, 2, 1, 2, 2, 3, 2, 1, 3]

maxRepititionEfficient(A)
