"""
Given an array of numbers, give an algorithm for 
finding the first element in the array which is 
repeated. For example, in the array = {3, 2, 1, 2, 2, 3},
the first repeated number is 3 (not 2). That means, 
we need to return the first element among the
repeated elements.
"""

A = [3, 2, 1, 2, 2, 3]


def firstRepeatedElement(A):
    for i, v in enumerate(A):
        for j, d in enumerate(A):
            if i != j and v == d:
                return f" Index: {i} and  value: {v}"
    return "No repeated!"


def firstRepeatedSort(A):
    A.sort()
    for i, v in enumerate(A):
        for j, d in enumerate(A):
            if i != j and v == d:
                return f" Index: {i} and  value: {v}"
    return "No repeated!"
    """
    Note sorting is not permited because 
    the order of the will change after sorting
    """


# def firstRepeatedHash(A):
#     table = {}
#     for i in A:
#         if i in table and table[i] == 1:
#             table[i] = -2
#         elif i in table and table[i] < 0:
#             table[i] -= 1
#         elif i != "":
#             table[i] = 1
#         else:
#             table[i] = 0
#     print(table)

def printFirstRepeating(a, n):
    for i in range(len(a)):
        if a.count(a[i]) > 1:
            return a[i]
    return "there is no repetition number"


# Driver code
# arr = [10, 5, 3, 4, 3, 5, 6]
# n = len(arr)
# print(printFirstRepeating(arr, n))

# def firstRepeatedHash(A):
#     helper = set()
#     for i in A:
#         if i in helper:
#             return i
#         else:
#             helper.add(i)


A = [3, 2, 1, 2, 2, 3]
# A = [3, 2, 1, 1, 2, 1, 2, 5, 5]
# x = firstRepeatedHash(A)
# print(x)

"""
Note not working the code right below"""
# def firstRepeatedElementAmongRepeatedElementsWithHash(A):
#     table = {}  # hash
#     max = 0
#     for element in A:
#         if element in table and table[element] == 1:
#             table[element] = -2
#         elif element in table and table[element] < 0:
#             table[element] -= 1
#         elif element != " ":
#             table[element] = 1
#         else:
#             table[element] = 0
#     for element in A:
#         if table[element] < max:
#             max = table[element]
#             maxRepeatedElement = element
#     print(maxRepeatedElement, "repeated for ", abs(max), " times")


# firstRepeatedElementAmongRepeatedElementsWithHash(A)
