A = [7,2,1,6,8,5,3,4]

def quick_sort(A,start, stop):
    if start >= stop:
        return
    pIndex = partition(A,start, stop)
    quick_sort(A, start, pIndex-1)
    quick_sort(A, pIndex+1, stop)
    # print(A)
    
def partition(A, start, stop):
    pivot = A[stop]
    pIndex = start
    for i in range(start, stop):
        if A[i] <= pivot:
            A[pIndex], A[i] = A[i], A[pIndex]
            pIndex += 1
    A[pIndex], A[stop] =  A[stop], A[pIndex]
    return pIndex

# partition(A,0,len(A)-1)
quick_sort(A,0, len(A)-1)
print(A)
