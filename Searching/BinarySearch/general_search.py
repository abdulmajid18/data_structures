# Search in2D sorted array
import collections
import sys
A = [[-1,2,4,4,6],
     [1,5,5,9,21],
     [3,6,6,9,22],
     [3,6,8,10,24],
     [6,8,9,12,25],
     [8,10,12,13,40]]
def search_2D_sorted_array(A,x):
    for i,row in enumerate(A):
        left = 0
        right = len(row) - 1
        while left <= right:
            mid = (right+left) // 2
            if row[mid] < x:
                left = mid + 1
            elif row[mid] > x:
                right = mid - 1
            else:
                return i,mid
    return -1, 0

# x, y = search_2D_sorted_array(A, 7)
# x, y = search_2D_sorted_array(A, 8)

def search_2D_optimized(A,x): 
    row, col = 0, len(A[0]) - 1
    while row < len(A) and col >= 0:
        if A[row][col] == x:
            return True
        elif A[row][col] < x:
            row += 1
        else:
            col -= 1
    return False

# x = search_2D_optimized(A,7)
# y = search_2D_optimized(A,9)
# print(x,y)


A = [3,2,5,1,2,4]

def find_min_max_simutanously_brute(A):
    mini = A[0]
    maxi = A[0]
    for i, v in enumerate(A):
        if A[i] < mini:
            mini = A[i]
        elif A[i] >= maxi:
            maxi = A[i]
    # print(mini, maxi)

MinMax = collections.namedtuple('MinMax', ('smallest', 'largest'))    
def find_min_max_simutanously(A):
    def min_max(a,b):
        return MinMax(a,b) if a < b else MinMax(b, a)
    
    if len(A) <= 1:
        return MinMax(A[0], A[0])
    
    global_min_max = min_max(A[0], A[1])
    for i in range(2, len(A)-1, 2):
        local_min_max = min_max(A[i], A[i+1])
        global_min_max = MinMax(
            min(global_min_max.smallest, local_min_max.smallest),
            max(global_min_max.largest, local_min_max.largest)
        )

    if len(A) % 2:
        global_min_max = MinMax(
            min(global_min_max.smallest, A[-1]),
            max(global_min_max.largest, A[-1])
        )
    return global_min_max
   

ans = find_min_max_simutanously(A)
print(ans)