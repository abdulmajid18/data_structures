def findMiniumInRotatedSoredArray(A):
    l = 0
    r = len(A) - 1
    while l <= r:
        m = (l + r) // 2
        if A[l] <= A[m] <= A[r]:
            # print(A[l])
            return A[l]
        if A[m] < A[l]:
            r = m
        else:
            l = m + 1


def findMin(nums) -> int:
    for i in range(1, len(nums)):
        if nums[i] < nums[0]:
            print(nums[i])
            return nums[i]
    return nums[0]


A = [15, 16, 19, 20, 25, 26, 27, 58, 69, 31, 1, 3, 4, 5, 7, 10, 14]
B = [-5,-3,-2,-6,-10,-12]
# print(findMiniumInRotatedSoredArray(A))
# findMin(B)
def findMiniumElementInRotatedSoredArray(A, k):
    l = 0
    r = len(A) - 1
    while l <= r:
        m = (l + r) // 2
        if A[m] == k:
            # print(A[l]) 
            return m
        if A[m] >= A[l]:
            if A[l] <= k < A[m]:
                r = m - 1
            else:
                l = m + 1
        else:
            if A[m] < k <= A[r]:
                l = m + 1
            else:
                r = m - 1
