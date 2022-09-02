A = [5,13,17]
B = [3,7,11,19,20]
i = 0
j = 0
k = 0
def merge_two_list_bruteforce(a,b):
    result = []
    while i < len(A) and j < len(B):
        if A[i] < B[j]:
            result.append(A[i])
            i += 1
        elif A[i] > B[j]:
            result.append(B[j])
            j += 1
    if i < len(A):
        for x in A[i:]:
            print(x)
            result.append(x)
    if j < len(B):
        for x in B[j:]:
            result.append(x)
    print(f"Results ...........{result}")

def merge_two_array_insertion_sort(A,B):
    for i,v1 in enumerate(B):
        for j, v2 in enumerate(A):
            pass


A = [5,13,17,0,0,0,0,0,0]
B = [3,7,11,19,20,22]
n = 3-1
m = 6-1
last_idx = len(A)-1
while n > -1 and m > -1:
    if A[n] < B[m]:
        A[last_idx] = B[m]
        m -= 1
    else:
        A[last_idx] = A[n]
        n -= 1
    last_idx -= 1
while m > -1:
    A[last_idx] = B[m]
    m, last_idx  = m-1, last_idx-1
print(A)



