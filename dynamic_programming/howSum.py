""" Returns possible numbers hat could sum up to a specific tartget"""

def howSum(target, elements):
    if target == 0:
        return 1
    if target < 0:
        return 0
    for num in elements:
        remainder = target -  num
        remainderResult  = howSum(remainder, elements)
        if remainderResult == 1:
            return [].append(num)
    return None

ans = howSum(7, [5,4,3,7])
print(ans)
