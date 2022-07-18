
import math
import sys


A = [1, 60, -10, 70, -80, 85]

# def twoElemenClosestToZeroA(A):
#     n = len(A)
#     for i


def twoElemenClosestToZero(A):
    n = len(A)
    if n < 2:
        print("Invalid Input")
        return
    minLeft = 0
    minRight = 1
    minSum = A[0] + A[1]
    for l in range(1, n-1):
        for r in range(l+1, n):
            sum = A[l] + A[r]
            if abs(minSum) > abs(sum):
                minSum = sum
                minLeft = l
                minRight = r
    print("The two elements whose sum is minimum are ",
          A[minLeft], A[minRight])


def twoElemenClosestToZeroB(A):
    n = len(A)
    A.sort()
    if n < 2:
        print("Invalid Input")
        return
    l = 0
    r = n - 1
    minLeft = l
    minRight = n - 1
    minSum = sys.maxsize
    while l < r:
        sum = A[l] + A[r]
        if abs(minSum) > abs(sum):
            minSum = sum
            minLeft = l
            minRight = r
        if sum < 0:
            l += 1
        else:
            r -= 1
    print("The two elements whose sum is minimum are ",
          A[minLeft], A[minRight])


twoElemenClosestToZeroB(A)
