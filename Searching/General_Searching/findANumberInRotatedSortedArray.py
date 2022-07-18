"""
Given a sorted array of integers that has been rotated 
an unknown number of times, give a O(logn) algorithm
that finds an element in the array. Example: 
Find 5 in array 
(15 16 19 20 25 1 3 4 5 7 10 14) 
Output: 8 (the index of 5 in the array)
"""


def findElementInRotatedSorted(A, x):
    left = 0
    right = len(A) - 1
    while left <= right:
        mid = (left + right) // 2
        if A[mid] == x:
            return mid
        elif A[mid] >= A[left]:
            if A[left] <= x <= A[mid]:
                right = mid - 1
            else:
                left = mid + 1
        else:
            if A[mid] < x < A[right]:
                left = mid + 1
            else:
                right = mid - 1

    return -1


# def findElementInRotatedSortedArrayRecursion(A, x):
#     if A == None or len(A) == 0:
#         return -1
#     low = 0
#     high = len(A) - 1
#     return findWithRecursion(A, x, low, high)


# def findWithRecursion(A, target, low, high):
#     if low > high:
#         return -1
#     mid = (low + high) // 2
#     if mid[A] == target:
#         return mid
#     if A[low] < A[high]:
#         if A[low] <= target <= A[mid]:
#             return findWithRecursion(A, target, left, mid + 1)
#         findWithRecursion(A, target, left + 1, mid)
#     elif A[low] > A[mid]:
#         if A[mid] < target <= A[high]:
#             return findWithRecursion(A, target, mid+1, high)
#         return findWithRecursion(A, target, low, mid-1)
#     else:
#         if A[mid] != A[high]:
#             return findWithRecursion(A, target, mid+1, high)
#         result = findWithRecursion(A, target, low, mid-1)
#         if result != -1:
#             return result
#     return findWithRecursion(A, target, mid+1, high)


# A = [15, 16, 19, 20, 25, 1, 3, 4, 5, 7, 10, 14]

# ans = findElementInRotatedSorted(A, 5)
# print(ans)
