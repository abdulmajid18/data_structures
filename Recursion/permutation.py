from typing import List
def permute(nums):
    result = []
    if len(nums) == 1:
        return [nums.copy()]
    
    for i in range(len(nums)):
        n = nums.pop(0)
        perms = permute(nums)
        
        for perm in perms:
            perm.append(n)  
        result.extend(perms)
        nums.append(n)
        
    return result

x = [1,2,3]

# ans = permute(x)

def permutations(A:List):
    result = []
    def directed_permutation(i):
        if i == len(A) - 1:
            result.append(A.copy())
            return 
        for j in range(i, len(A)):
            A[i], A[j] = A[j], A[i]
            directed_permutation(i+1)
            A[i], A[j] = A[j], A[i]
    directed_permutation(0)
    return result

ans = permutations(x)
print(ans)