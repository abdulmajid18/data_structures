A = [1,2,3,4]
B = [7,8,9,10]

def merge(left, right):
    result = []
    i, j = 0, 0
    while i < len(left) and j < len(right):
        if left[i] < right[j]:
            result.append(left[i])
            i += 1
        else:
            result.append(right[j])
            j += 1
    while (i < len(left)):
        result.append(left[i])
        i += 1
    while (j < len(right)):
        result.append(right[j])
        j += 1
    return result

def find_median(A,B):
    result = merge(A,B)
    mid = len(result) // 2
    print(result[mid])

def find_median_2(A,B):
    m1 = len(A) // 2
    m2 = len(B) //2
    if A[m1] == B[m2]:
        return A[m1]
