""" Given an array of n numbers, give an algorithm for finding 
a contigious subsequence A(i) ..... A(j)"""

import itertools
A = [-2, 11, -4, 18, -5, 2] 
# Ans --> 20

def max_contigious_brute(A):
    maxSum = 0
    n = len(A)
    for i in range(n):
        for j in range(i, n):
            current_sum = 0
            for k in range(i, j+1):
                current_sum += A[k]
                if current_sum > maxSum:
                    maxSum = current_sum
    return maxSum

def max_contigious2(A):
    maxSum = 0
    n = len(A)
    for i in range(1, n):
        current_sum = 0
        for j in range(i,n):
            current_sum += A[j]
            if current_sum > maxSum:
                maxSum = current_sum
    return maxSum

def max_subarray_dp(arr):
    max_here = max_so_far = 0
    for x in arr:
        max_here = max(x, max_here+x)
        max_so_far = max(max_so_far, max_here)
    print(max_so_far)
    return max_so_far
A = [-2, 11, -4, 18, -5, 2] 

def max_subarray_dp_2(arr):
    sum_here = sum_so_far = 0
    for i in range(len(arr)):
        sum_here = sum_here + arr[i]

        if sum_here < 0:
            sum_here = max(sum_here, sum_so_far)
        if sum_so_far < sum_here:
            sum_so_far = sum_here
    print(sum_so_far)


def find_max_contigious(A):
    max_sum =  min_sum = 0
    n = len(A)
    for running_sum in itertools.accumulate(A):
        min_sum = min(min_sum, running_sum)
        max_sum = max(max_sum, running_sum-min_sum)
        print(f"Min: {min_sum}, max: {max_sum} diff: {running_sum-min_sum}")
        
        
    print(f"Ans: {max_sum}")

A = [12, 11, -4, 18, -5, 2] 
# Ans --> 20   
def max_contigious_space(A):
    max_sum = 0
    n = len(A)
    M = [0] * (n)
    if A[0] > 0:
        M[0] = A[0]
    else:
        M[0] = 0
    for i in range(1,n):  
        if (M[i-1] + A[i]) > 0:
            M[i] = M[i-1] + A[i]
        else:
            M[i] = 0
    for j in range(n):
        if M[j] > max_sum:
            max_sum = M[j]
    print(max_sum)

max_subarray_dp_2(A)
max_subarray_dp(A)