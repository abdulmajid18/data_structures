def checkDuplicateBruteForce(A):
    for i in range(0, len(A)):
        for j in range(i+1, len(A)):
            if A[i] == A[j]:
                print("Duplicate at index ", i, A[i])
                return
    print("No duplicates in the array")


def checkDupicateSorting(A):
    A.sort()
    for i in range(0, len(A)):
        for j in range(i+1, len(A)):
            if A[i] == A[j]:
                print("Duplicate at index ", i, A[i])
                return


B = [3, 2, 10, 20, 22, 32]
A = [4, 5, 5, 6, 9, 9, 9, 8, 2, 3]
checkDuplicateBruteForce(B)
