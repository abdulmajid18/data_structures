# from collections import namedtuple 

# key = namedtuple('key', ('m', 'n'))   
def grid_traversal(m, n, memo = {}):
    key = str(m) + ',' + str(n)
    if key in memo:
        return memo[key]
    if m == 1 and n == 1:
        return 1
    if m == 0 or n == 0:
        return 0
    memo[key] =  grid_traversal(m - 1, n, memo) + grid_traversal(m, n - 1, memo)
    return memo[key]

ans = grid_traversal(500,200)
print(ans)
