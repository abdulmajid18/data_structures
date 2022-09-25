import operator
import random
import pprint
A = [
    [5,19,11,14],
    [31,9,6,22],
    [3,8,12,2],
    [21,3,4,28]
]
def peakIn2DBruteForce(A):
    # left, right, up, bottom = 0,0,0,0
    for i in range(len(A)):
        for j in range(len(A[0])):
            left, right, up, bottom = 0,0,0,0
            left, right, up, bottom = 0,0,0,0
            if j > 0:
                left = A[i][j - 1]
            if j < len(A) - 1:
                right = A[i][j + 1]
            if i > 0:
                up = A[i - 1][j]
            if i < len(A) - 1:
                bottom= A[i + 1][j]
            if (left <= A[i][j] >= right) and (up <= A[i][j] >= bottom):
                return (i, j, A[i][j])
A = [ [0, 9, 4, 2, 5, 6, 7],
 [7, 6, 8, 7, 2, 1, 8],
 [4, 9, 8, 9, 7, 5, 8],
 [2, 7, 6, 3, 6, 6, 0],
 [7, 3, 0, 6, 4, 5, 8],
 [6, 4, 5, 2, 6, 9, 6]]

A = [
    [51,19,11,519],
    [61,9,60,22],
    [73,81,120,42],
    [21,3,400,208]
]



def generate2DArray(n=7, m=7, lower=0, upper=9):
    return [[random.randint(lower, upper) for _ in range(m)] for _ in range(n)]

# if __name__ == '__main__':
#     matrix = generate2DArray(upper=9)
#     pprint.pprint(A)
#     x = peakIn2DBruteForce(A)
#     pprint.pprint(x)
""" Note the greedy Algorithm doesnt give the best complexiy it is 
the same complexity as he brute force solution with O(mn)"""

def greedyAscent(A):
    j = len(A[0]) // 2
    i = len(A) // 2
    while True:
        left, right, up,bottom = 0,0,0,0
        if j > 0:
            left = A[i][j-1]
        if j < len(A) - 1:
            right = A[i][j + 1]
        if i > 0:
            up = A[i - 1][j]
        if i < len(A) - 1:
            bottom= A[i + 1][j]
        if (left <= A[i][j] >= right) and (up <= A[i][j] >= bottom):
            return (i, j, A[i][j])
        mylist = [left, up, right, bottom]
        maxNeighborIndex, maxNeighborValue = max(enumerate(mylist), key=operator.itemgetter(1))
        if maxNeighborIndex == 0:
            j = j - 1
        elif maxNeighborIndex == 1:
            i = i - 1
        elif maxNeighborIndex == 2:
            j = j + 1
        else:
            i = i + 1



def peak_divide_conquer(A):
    j = len(A[0]) // 2
    maxvalue, rowmax = -1, -1
    for row in range(len(A)):
        if maxvalue <= A[row][j]:
            maxvalue = A[row][j]
            rowmax = row
    print(rowmax, j, maxvalue)
    left, right = -1, -1
    if j > 0:
        left = A[rowmax][j-1]
    if j < len(A[0])-1:
        right = A[rowmax][j+1]
    if left <= maxvalue >= right:
        return (rowmax, j, maxvalue)
    if left > maxvalue:
        half = []
        for row in A:
            half.append(row[:j+1])
        return peak_divide_conquer(half)
    if right > maxvalue:
        half = []
        for row in A:
            half.append(row[j:])
        return peak_divide_conquer(half)


if __name__ == '__main__':
    matrix = generate2DArray(upper=9)
    pprint.pprint(A)
    x = peak_divide_conquer(A)
    pprint.pprint(x)
