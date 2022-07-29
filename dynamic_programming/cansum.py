"""
Write a functon that takes in a targetsum
and an array of nubers as argument.

The function should return a boolean indicating
whather or not it is possibe to generate the 
targetsum using numbers from the array
"""




def canSum(target_sum, elements,memo = {}):
    if target_sum in memo:
        return memo[target_sum]
    if target_sum == 0: 
        return True
    if target_sum < 0:
        return False
    for num in elements:
        remainder = target_sum - num
        if canSum(remainder, elements, memo):
            memo[target_sum] = True
            return True
    memo[target_sum] = False
    return False

print(canSum(300, [7,14]))