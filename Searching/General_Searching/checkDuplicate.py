"""
Given an array ofn numbers, give an algorithm for cheking whether there are
any duplicate elements in the array or no
"""


def checkDuplicateBruteForce(A):
    for i in range(0, len(A)):
        for j in range(i+1, len(A)):
            if A[i] == A[j]:
                print("Duplicate exist: ", A[i])
                return
    print("No duplicates in given array.")


def checkDuplicateBruteForceB(A):
    for i, v1 in enumerate(A):
        for j, v2 in enumerate(A):
            if (i != j) and (v1 == v2):
                print("DUplicate Exist: ", v1)
                return
    print("No Duplicate exist")


def checkDuplicateSorting(A):
    A.sort()
    for i in range(0, len(A)):
        for j in range(i+1, len(A)):
            if A[i] == A[j]:
                print("Duplicate exist: ", A[i])
                return
    print("No duplicates in given array.")


def checkDuplicateHash(A):
    table = {}
    for element in A:
        if element in table:
            print("Duplicate exist: ", element)
            return
        elif element != "":
            table[element] = 1
        else:
            table[element] = 0
    print("No duplicates in given array.")


def checkDuplicateEfficientNegationTechnique(A):
    for i in range(0, len(A)):
        if A[abs(A[i])] < 0:
            print("Duplicate exist")
            return
        else:
            A[abs(A[i])] = -1
    print("No duplcate in the given array!")


A = [3, 2, 10, 20, 22, 32, 32]

checkDuplicateHash(A)
