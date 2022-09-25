
A = [534, 246, 933, 127, 277, 321, 454, 565, 220]

def merge(l1, l2):
    result = []
    i, j = 0, 0
    while i < len(l1) and j < len(l2):
        if l1[i] < l2[j]:
            result.append(l1[i])
            i += 1
        else:
            result.append(l2[j])
            j += 1
    while i < len(l1):
        result.append(l1[i])
        i += 1
    while j < len(l2):
        result.append(l2[j])
        j += 1
    print(result)

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
    
def merge_sort(A):
    if len(A) < 2:
        return A[:]
    else:
        middle = len(A) // 2
        left = merge_sort(A[:middle])
        right = merge_sort(A[middle:])
        return merge(left, right)
l1 = [1,3,5,7]
l2 = [2,4,6,8]

ans = merge_sort(A)
print(ans)
