"""
Find the two repeating elements in a given array"""


from itertools import product
from math import factorial, prod


def printTwoRepeatedElementsBruteForce(A):
    n = len(A)
    for i in range(0, n):
        for j in range(i+1, n):
            if(A[i] == A[j]):
                print(A[i])


a = [4, 2, 4, 5, 2, 3, 1]
# A = [3, 5, 7, 4, 2, 4, 2, 1, 9, 8, 6]
A = [1, 2, 2, 3, 3, 4, 5]


def printTwoRepeatedElementsSort(A):
    A.sort()
    n = len(A)
    for i in range(0, n):
        for j in range(i+1, n):
            if(A[i] == A[j]):
                print(A[i])


def printTwoRepeatedElementsHashA(A):
    table = {}
    for element in A:
        if element in table:
            table[element] += 1
        elif element != "":
            table[element] = 1
        else:
            table[element] = 0
    flag = 0
    for element in A:
        if flag == 2:
            break
        if table[element] == 2:
            print(element)
            flag += 1


def printTwoRepeatedElementsHashB(A):
    table = {}
    for element in A:
        if element in table and table[element] == 1:
            print(element)
            table[element] += 1
        elif element in table:
            table[element] += 1
        elif element != "":
            table[element] = 1
        else:
            table[element] = 0


# def sumAndFact(A):
#     x, y = 0, 0
#     summ = sum(A)
#     print(summ)
#     n = len(A)-2
#     print(n)
#     sumz = int(n*(n+1) / 2)
#     print(sumz)
#     fact = factorial(n)
#     prodd = prod(A)
#     diff = summ-sumz
#     pro = int(prodd/fact)

#     print(diff, pro)


# sumAndFact(A)
