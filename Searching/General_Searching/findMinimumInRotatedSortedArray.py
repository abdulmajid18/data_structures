def findMiniumInRotatedSoredArray(A):
    l = 0
    r = len(A) - 1
    while l <= r:
        m = (l + r) // 2
        if A[l] <= A[m] <= A[r]:
            return A[l]
        if A[m] < A[l]:
            r = m
        else:
            l = m + 1


def findMin(self, nums) -> int:
    for i in range(1, len(nums)):
        if nums[i] < nums[0]:
            return nums[i]
    return nums[0]


A = [15, 16, 19, 20, 25, 26, 27, 58, 69, 31, 1, 3, 4, 5, 7, 10, 14]
print(findMiniumInRotatedSoredArray(A))
