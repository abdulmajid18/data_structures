A = [12,2,1,15,2,4]

def smallest_nonconstructible(A):
    max_constructible = 0
    for a in sorted(A):
        if a > max_constructible + 1:
            break
        max_constructible += A
    return max_constructible + 1

ans = smallest_nonconstructible(A)
print(ans)