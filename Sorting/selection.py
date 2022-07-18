A = [10, 4, 43, 5, 57, 91, 45, 9, 7]


def selectionA(A):
    n = len(A)
    for i in range(n):
        for j in range(i+1, n):
            if A[j] < A[i]:
                A[j], A[i] = A[i], A[j]


def selectionB(A):
    suffixSt = 0
    while suffixSt != len(A):
        for i in range(suffixSt, len(A)):
            if A[i] < A[suffixSt]:
                A[suffixSt], A[i] = A[i], A[suffixSt]
        suffixSt += 1


selectionB(A)
print(A)
