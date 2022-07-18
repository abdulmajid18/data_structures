
A = [8, 6, 1, 2, 3, 4, 7, 5, 9]


def alternationA(A):
    A.sort()
    h = len(A) // 2
    for i in range(len(A)):
        if (i + 1) % 2 == 0:
            A[i], A[i+1] = A[i+1], A[i]
        else:
            continue
    return A


def rearrange(A):
    for i in range(len(A)):
        A[i:i + 2] = sorted(A[i:i+2], reverse=i % 2)
    return A


# x = sorted(A[0:0+2], reverse=0 % 2)
# print(A)
# print(x)
x = alternationA(A)
y = rearrange(A)
print(y)
print(x)
