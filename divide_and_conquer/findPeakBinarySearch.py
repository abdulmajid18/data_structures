A = [35, 5, 20, 2, 40, 25, 80, 25, 15, 40]


def findPeak(A):
    if not A:
        return -1
    left, right = 0, len(A) - 1
    while left + 1 < right:
        mid = left + (right - left) // 2
        if A[mid] < A[mid - 1]:
            right = mid
        elif A[mid] < A[mid + 1]:
            left = mid
        else:
            return mid
    mid = left if A[left] > A[right] else right
    return mid

# peak = findPeak(A)
# print("A \n", A[peak])


def findPeakBinarySearch(A):
    if not A:
        return -1
    left = 0
    right = len(A)-1
    while left + 1 < right:
        mid = (left + right) // 2
        if A[mid] < A[mid-1]:
            right = mid
        elif A[mid] < A[mid+1]:
            left = mid
        else:
            return A[mid]


# ans = findPeakBinarySearch(A)
# print(ans)

def findpeak_brute_force(A):
    peak = 0
    for i in range(len(A)):
        mid = i
        if i == 0:
            prev = 0
            next = i + 1
        elif i == len(A) - 1:
            prev = i - 1
            next = i
        else:
            prev = i - 1
            next = i + 1
        if A[mid] >= A[prev] and  A[mid] >= A[next]:
            if A[mid] > peak:
                peak = A[mid]
    print(peak)
A = [35, 5, 20, 2, 25, 80, 25, 15, 40]

def find_peak_brute_2(A):
    n = len(A)
    maxPeak = maxIndex = 0
    peak = A[0]
    index = 0
    for i in range(1,n-2):
        prev = A[i - 1]
        mid  = A[i]
        next = A[i + 1]

        if mid > prev and mid > next:
            index = i
            peak = mid
        if peak > maxPeak:
            maxIndex, maxPeak = index,peak
    return maxPeak

# Using divide and conquer
# A = [i for i in range(1,21)]
def find_peak_divide_and_conquer(A):
    n = len(A)
    left = 0
    right = n - 1

    while left + 1 < right:
        mid = (left + right) // 2
        if A[mid] < A[mid-1]:
            right = mid
        elif A[mid] < A[mid+1]:
            left = mid
        else:
            return A[mid]
    mid = left if A[left] > A[right] else right
    return A[mid]
ans = find_peak_divide_and_conquer(A)
print(ans)
