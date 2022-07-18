"""
Given an array of n
elements. Find two elements in the array such 
that their sum is equal to given element
"""


def twoElementSumBruteForce(A, element):
    for i in range(len(A)):
        for j in range(i+1, len(A)):
            if A[i] + A[j] == element:
                return A[i], A[j]
    return 0


A = [1, 4, 45, 6, 10, -8]
# A.sort()


def twoElementSumNlogn(A, element):
    # Assuming array is sorted
    loIndex = 0
    hiIndex = len(A) - 1

    while loIndex < hiIndex:
        if A[loIndex] + A[hiIndex] == element:
            return A[loIndex], A[hiIndex]
        elif A[loIndex] + A[hiIndex] < element:
            loIndex += 1
        else:
            hiIndex -= 1
    return 0


# print(twoElementSumNlogn(A, 16))
def printTwoRepeatedElementsHash(A, K):
    table = {}  # hash
    for element in A:
        if element in table:
            table[element] += 1
        elif element != " ":
            table[element] = 1
        else:
            table[element] = 0
    for element in A:
        if K-element in table:
            print("yes-->", element, "+", K-element, " = ", K)


printTwoRepeatedElementsHash(A, 16)
