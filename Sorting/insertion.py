A = [10, 4, 43, 5, 57, 91, 45, 9, 7]
L = [1, 3, 5, 7, 2, 6, 25, 18, 13]


def insertionA(A):
    for i in range(1, len(A)):
        temp = A[i]
        while A[i-1] > temp and i > 0:
            A[i], A[i-1] = A[i-1], A[i]
            i = i - 1
    return A

# def insertionB(A):
#     for i in range(1, len(A)):
#         temp = A[i]
#         k = i
#         while k > 0 and temp < A[i-1]:
#             A[k] = A[k-1]
#             A[k] = temp
#             k -= 1

#     return A


ans = insertionA(A)
print(ans)
