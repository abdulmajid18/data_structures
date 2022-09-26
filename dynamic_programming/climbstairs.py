def climbStairs(n: int) -> int:
    if n == 0 :
        return 1
    elif n < 0:
        return 0
    ans = climbStairs(n-1 ) + climbStairs(n-2)
    
    return ans

for i in range(4,-1,-1):
    print(i)