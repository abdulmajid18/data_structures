
import random

x = [3, 7, 5, 11]


def sampleOnlineData(A, k):
    for i in range(k):
        r = random.randint(i, len(A) - 1)
        A[i], A[r] = A[r], A[i]
    return A[:k]


# ans = sampleOnlineData(x, 3)
# print(ans)
