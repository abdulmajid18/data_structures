import math

def binarySearchIterative(elements, element):
    low = 0
    high = len(elements)-1
    while low <= high:
        mid = (low+high)//2

        mid = low + (high-low) / 2
        if elements[mid] > element:
            high = mid-1
        elif elements[mid] < element:
            low = mid+1
        else:
            return mid
    return -1


def binarySearchRecursive(elements, element, low, high=-1):
    if not elements:
        return -1
    if high == -1:
        high = len(elements)-1
    if high == low:
        if elements[low] == element:
            return low
        else:
            return -1
    mid = (low+high) // 2
    if elements[mid] > element:
        return binarySearchRecursive(elements, element, low, mid-1)
    elif elements[mid] < element:
        return binarySearchRecursive(elements, element, mid+1, high)
    else:
        return mid


# A = [534, 246, 933, 127, 277, 321, 454, 565, 220]
# A.sort()
# print(A)
# # print(binarySearchIterative(A, 277))
# print(binarySearchRecursive(A, 277, 0))

A = [-14,-10,2,108,108,243,285,285,401]

def search_first_occurence(A, k):
    low = 0
    high = len(A) - 1
    result = -1
    while low <= high:
        mid = low + (high-low) // 2
        if A[mid] < k:
            low = mid + 1
        elif A[mid] == k:
            result = mid 
            high = mid - 1
        else:
            high = mid - 1
    return result

# ans = search_first_occurence(A,108)
# print(ans)

def search_sorted_index_equals_element_brute(A):
    for i,v in enumerate(A):
        if i == v:
            return i
A =[-2,0,2,3,6,7,9]
# ans = search_sorted_index_equals_element_brute(A)
# print(ans)


def search_sorted_index_equals_element(A):
    low, high = 0, len(A) - 1
    while low <= high:
        mid = low + (high-low) //2
        difference = A[mid] - mid
        if difference == 0:
            return mid
        elif difference > 0:
            high = mid - 1
        else:
            low = mid + 1
    return -1

# ans = search_sorted_index_equals_element(A)
# print(ans)

"""Brute force O(n)"""
A = [378,478,550,631,103,203,220,234,279,368]
def cyclically_sorted_array(A):
    for i,v in enumerate(A):
        if A[i+1] < v:
            return i+1
# ans = cyclically_sorted_array(A)
# print(ans)
 
def cyclically_sorted_array(A):
    left = 0
    right = len(A) - 1
    while left < right:
        mid = (right+left) // 2
        if A[mid] > A[right]:
            left = mid + 1
        else:
            right = mid
    return left

# ans = cyclically_sorted_array(A)
# print(ans)
A = []
for i in range(1,21):
    A.append(i)
def square_root(A,k):
    """Pass a number (k) and generate a number in Array A  whose square root
    is <= K  """
    left, right = 0, k
    while left <= right:
        mid = (right+left) // 2
        mid_square = mid * mid
        if mid_square <= k:
            left = mid + 1
        else:
            right = mid - 1
    return left 

# ans = square_root(A,21)
# print(ans)

def generate_square_root(x):
    """I implements a function that takes a floating point input
    and returns a square root"""
    left, right = (x, 1.0) if x < 1.0 else (1.0, x)

    # Keep searching as ong as left != right
    while not math.isclose(left, right):
        mid = 0.5 * (left + right)
        mid_square = mid * mid
        if mid_square > x:
            right = mid
        else:
            left = mid
    return left

