# Search in2D sorted array
import collections
from itertools import count
import random
import sys
A = [[-1,2,4,4,6],
     [1,5,5,9,21],
     [3,6,6,9,22],
     [3,6,8,10,24],
     [6,8,9,12,25],
     [8,10,12,13,40]]
def search_2D_sorted_array(A,x):
    for i,row in enumerate(A):
        left = 0
        right = len(row) - 1
        while left <= right:
            mid = (right+left) // 2
            if row[mid] < x:
                left = mid + 1
            elif row[mid] > x:
                right = mid - 1
            else:
                return i,mid
    return -1, 0

# x, y = search_2D_sorted_array(A, 7)
# x, y = search_2D_sorted_array(A, 8)

def search_2D_optimized(A,x): 
    row, col = 0, len(A[0]) - 1
    while row < len(A) and col >= 0:
        if A[row][col] == x:
            return True
        elif A[row][col] < x:
            row += 1
        else:
            col -= 1
    return False

# x = search_2D_optimized(A,7)
# y = search_2D_optimized(A,9)
# print(x,y)


A = [3,2,5,1,2,4]

def find_min_max_simutanously_brute(A):
    mini = A[0]
    maxi = A[0]
    for i, v in enumerate(A):
        if A[i] < mini:
            mini = A[i]
        elif A[i] >= maxi:
            maxi = A[i]
    # print(mini, maxi)

MinMax = collections.namedtuple('MinMax', ('smallest', 'largest'))    
def find_min_max_simutanously(A):
    def min_max(a,b):
        return MinMax(a,b) if a < b else MinMax(b, a)
    
    if len(A) <= 1:
        return MinMax(A[0], A[0])
    
    global_min_max = min_max(A[0], A[1])
    for i in range(2, len(A)-1, 2):
        local_min_max = min_max(A[i], A[i+1])
        global_min_max = MinMax(
            min(global_min_max.smallest, local_min_max.smallest),
            max(global_min_max.largest, local_min_max.largest)
        )

    if len(A) % 2:
        global_min_max = MinMax(
            min(global_min_max.smallest, A[-1]),
            max(global_min_max.largest, A[-1])
        )
    return global_min_max
   

# ans = find_min_max_simutanously(A)
# print(ans)
A = [3,2,1,5,4]

# def kth_largest_element_in_array1(A:list, k):
#     sorted_arr = sorted(A)
#     print(sorted_arr)
#     print(sorted_arr[k-1])

# kth_largest_element_in_array1(A,1)
def kth_largest_element_in_array2(A:list, k):
    sorted_arr = sorted(A)
    sorted_arr.reverse()
    print(sorted_arr)
    print(sorted_arr[k-1])
    # return sorted_arr[k-1]

# kth_largest_element_in_array2(A,1)

def kth_largest_element_in_array3(A:list, k):
    hash_table = []
    new = A  
    for j in range(len(A)-1):     
        maxi = -1
        for i,v in enumerate(new):
            if v > maxi:
                maxi = v
        hash_table.append(maxi)
        new.remove(maxi)
    last = new[-1]
    hash_table.append(last)
    print(hash_table)
    print(new)
# kth_largest_element_in_array3(A,1)

def kth_largest_element_in_array_bubblesort(L,k):
    for i in range(len(L)):
        for j in range(1, len(L)):
            if L[j-1] > L[j]:
                temp = L[j]
                L[j] = L[j-1]
                L[j-1] = temp
    k = len(A)-k
    print(L[k])

# kth_largest_element_in_array_bubblesort(A,2)
# kth_largest_element_in_array2(A,1)
# def kth_largest_element_in_array3(A, k):
#     def partition_around_pivot(left, right, pivot_idx):
#         pass
# B = [8,1,3,2,6,7]
# def kth_largest_element_in_array_mx_heap(A,k):
#     """In max heap we need the smallest so we get rid of maxi"""


# kth_largest_element_in_array2(A,4)
"""Check duplicate """
# brute force
A = [3,2,10,20,22,32]

def checkDuplicateBruteForce(A):
    n = len(A)
    for i, v1 in enumerate(A):
        for j, v2 in enumerate(A):
            if j == i:
                continue
            if v1 == v2:
                print(f"Index {i} element {v2}")
                return
    print("No duplicate found")
A = [3,2,1,2,2,3]
# checkDuplicateBruteForce(A)
def checkDuplicateSorting(A):
    A.sort()
    for i, v1 in enumerate(A):
        for j, v2 in enumerate(A):
            if j == i:
                continue
            if v1 == v2:
                print(f"Index {j} element {v2}")
                return
    print("No duplicate found")

A = [3,2,1,2,2,3]

def checkDuplicateHashing(A):
    hash_table = {}
    for element in A:
        if element in hash_table:
            hash_table[element] += 1
            print(f"Duplicate found {element}")
        elif element not in hash_table:
            hash_table[element] = 1
    print(f"Hash table is {hash_table}")
            
# checkDuplicateHashing(A)

"""Given an array of elemennts find the elementt with
the maximum occurence"""
def maxRepititonsBruteForce(A):
    n = len(A)
    count = maxi = 0
    for i in range(0, n):
        count = 1
        for j in range(i+1, n):
            if A[i] == A[j]:
                count += 1
        if maxi < count:
            maxi = count
            element = A[i]
    print(f"Maximum of {element} is {maxi} occurance")
A = [3, 2,1,2,2,3,2,1,3]
# maxRepititonsBruteForce(A)

def maxRepititionSort(A):
    A.sort()
    count = maxi = 1
    element = A[0]
    for i in range(1, len(A)):
        if A[i] == element:
            count += 1
            if count > maxi:
                maxi = count
                max_element = element
        else:
            count = 1
            element = A[i]
    print(f"Maximum of {max_element} is {maxi} occurance")

# maxRepititionSort(A)

def maxRepititionHash(A):
    hash_table = {}
    for element in A:
        if element in hash_table:
            hash_table[element] += 1
        else:
            hash_table[element] = 1
    maxi = element  = 0
    for element in A:
        if hash_table[element] > maxi:
            maxi = hash_table[element]
            max_element = element
    print(f"Maximum of {max_element} is {maxi} occurance")

# maxRepititionHash(A)


"""First repeaed element in an array [3,2,1,2,2,3]
The first repeatted is 3 not 2"""

def firstRepeatedBruteForce(A):
    n = len(A)
    for i in range(n):
        for j in range(i, n):
            if A[i] == A[j]:
                print(f"found Index:{i} element{A[i]}")
                return
A = [3,2,1,2,2,3]
# firstRepeatedBruteForce(A)

def firstRepeattedWIthHash(A):
    table = {}
    max =  -1000
    max_element = 0
    for element in A:
        if element in table and table[element] == 1:
            table[element] = -2
        elif element in table and table[element] < 0:
            table[element] -= 1
        elif element != " ":
            table[element] = 1
        else:
            table[element] = 0
    print(table)
    for element in A:
        if table[element] < 0:
            if table[element] > max:
                max = table[element]
                max_element = element
    print(f"First Repeated of {max_element} is {abs(max)} occurance")

# A = [3,2,1,1,2,1,2,5,5]
# firstRepeattedWIthHash(A)

"""Find missing number"""
def findMissingNumberBrute(A):
    n = len(A)
    for i in range(1, n+2):
        found = 0
        for j in range(0,n):
          if i == A[j]:
            found = 1
        if found == 0:
            print("Missing number is ", i)
# findMissingNumber([1,2,4,6,3,7,8])
def findMissingNumberSort(A):
    n = len(A)
    A.sort()
    print(A)
    for i in range(len(A)-1):
        if A[i]+1 != A[i+1]:
            print("Missing number is", A[i]+1)

A = [1,2,4,6,3,7,8]
A = [8,2,1,4,6,5,7,9]

from collections import defaultdict
def findMissingNumber2(A):
    d = defaultdict(int)
    n = len(A)
    for element in A:
        d[element] += 1
    print(d)
    for element in range(1, n+1):
        if d[element] == 0:
            print(element)
            return element
        else:
            d[element] -= 1

def findMissingNumberSummation(A):
    n = len(A) + 1
    print(n)
    sum_expected = n * (n+1) // 2
    sum_actual = sum(A)
    print(sum_expected-sum_actual)


def twoElementsWithSumK_nlogn(A, k):
    A.sort()
    low = 0
    high = len(A)-1
    
    while low < high:
        # print(A[low], A[high])
        if (A[low] + A[high] == k):
            return 1
        elif (A[low] + A[high] < k):
            low += 1
        else:
            high -= 1
    return 0
A = [1,4,45,6,10,-8]
# ans = twoElementsWithSumK_nlogn(A,46)
A = [3,2,1,5,6,4]
def kth_largest_element_in_array_quick_select_1(A,k):
    def partition(A, start, stop):
        pivot = A[stop]
        pIndex = start
        for i in range(start, stop):
            if A[i] <= pivot:
                A[pIndex], A[i] = A[i], A[pIndex]
                pIndex += 1
        A[pIndex], A[stop] =  A[stop], A[pIndex]

        index = len(A)-k  
        if pIndex > index:
            return  partition(A,start,pIndex-1)
        elif pIndex < index:
            return partition(A,pIndex+1,stop)
        else:
            return A[pIndex]
    return partition(A, 0, len(A)-1)

import random
def kth_largest_element_in_array_quick_select_2(A,k):
    def partition(A, start, stop, pivot_idx):
        pivot_value = A[pivot_idx]
        new_pivot_idx = start
        for i in range(start, stop):
            
            if A[i] <= pivot_value:
                A[new_pivot_idx], A[i] = A[i], A[new_pivot_idx]
                new_pivot_idx += 1
        A[new_pivot_idx], A[stop] =  A[stop], A[new_pivot_idx]
        return new_pivot_idx

    start = 0
    stop = len(A)-1

    while start <= stop:
        pivot_idx = random.randint(start, stop)
        new_pivot_idx = partition(A, start, stop, pivot_idx)
        if new_pivot_idx == k - 1:
            return A[new_pivot_idx]
        elif new_pivot_idx > k - 1:
            stop = new_pivot_idx - 1
        else:
            start = new_pivot_idx + 1


# ans = kth_largest_element_in_array_quick_select(A,2)
# print(ans)

