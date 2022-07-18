# Search in2D sorted array

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

x = search_2D_optimized(A,7)
y = search_2D_optimized(A,9)
print(x,y)
