def bubble_sort(L):
    swap = False
    while not swap:
        swap = True
        for j in range(1, len(L)):
            if L[j-1] > L[j]:
                swap = False
                temp = L[j]
                L[j] = L[j-1]
                L[j-1] = temp


def bubbleSort(L):
    for i in range(len(L)):
        for j in range(1, len(L)):
            if L[j-1] > L[j]:
                temp = L[j]
                L[j] = L[j-1]
                L[j-1] = temp


def bubbleSortA(A):
    for passnum in range(len(A)-1, 0, -1):
        print(passnum)
        for i in range(passnum):
            if A[i] > A[i+1]:
                A[i], A[i+1] = A[i+1], A[i]


# def bubbleSortB(L):
#     swapped = 1
#     for passnum in range(len(A)-1, 0, -1):
#         if (swapped == 0):
#             return
#         for i in range(passnum):
#             if A[i] > A[i+1]:
#                 A[i], A[i+1] = A[i+1], A[i]
#                 swapped = 1


# def bubbleSortC(L):
#     swapped = 1
#     for i in range(len(L)):
#         if swapped == 0:
#             return
#         for j in range(len(A)-1, i, -1):
#             if L[j-1] > L[j]:
#                 temp = L[j]
#                 L[j] = L[j-1]
#                 L[j-1] = temp
#                 swapped = 1


A = [10, 4, 43, 5, 57, 91, 45, 9, 7]
L = [1, 3, 5, 7, 2, 6, 25, 18, 13]

bubbleSortA(A)
print(A)
