def threeElementWithSumKBruteForce(A, K):
    n = len(A)
    for i in range(0, n-2):
        for j in range(i+1, n-1):
            for k in range(j+1, n):
                if A[i] + A[j] + A[k] == K:
                    print("yes-->", A[i], " + ", A[j], " + ", A[k], " = ", K)
                    return 1
    return 0


def threeElementWithSumSorting(A, K):
    n = len(A)
    left = 0
    right = n - 1
    for i in range(0, n-2):
        left = i + 1
        right = n - 1
        while left < right:
            print(A[i] + A[left] + A[right], K)
            if(A[i] + A[left] + A[right] == K):
                print("yes-->", A[i], " + ", A[left],
                      " + ", A[right], " = ", K)
                return 1
            elif(A[i] + A[left] + A[right] < K):
                left += 1
            else:
                right -= 1
    return 0


A = [1, 6, 45, 4, 10, 18]
A.sort()
ans = threeElementWithSumSorting(A, 20)
print(ans)
