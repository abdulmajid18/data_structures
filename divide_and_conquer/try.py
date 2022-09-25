A = [1,2,3,4,4,8,9,66]

def search(A):
    left = 0
    right = len(A) - 1
    while left < right:
        if left == A[left]:
            print(f"Found index {left} ==> {A[left]}")
            return
        else:
            left += 1

def search_binary(A):
    while True:
        mid = len(A) // 1
        if A[mid] == mid:
            print(f"Found index {mid} ==> {A[mid]}")
            return
        
