"""Let and be two arrays of elements each. Given a number , give an O(
whether there exists a ∈ A and b ∈ B such that a + b =  K.
Solution: Since we need O(nlogn) time algorithm for determining"""


def binarySearchIterative(A, element):
    left = 0
    right = len(A)-1
    while left <= right:
        middle = left + right // 2
        if element > A[middle]:
            left = middle + 1
        elif element < A[middle]:
            right = middle - 1
        else:
            return middle
    return -1


def findExistence(A, B, k):
    A.sort()
    for i, x in enumerate(A):
        b = k-x
        ans = binarySearchIterative(B, b)
        if ans == -1:
            return 0
    return 1


A = [2, 3, 5, 7, 12, 15, 23, 32, 42]
B = [3, 13, 13, 15, 22, 33]

ans = findExistence(A, B, 270)
print(ans)
