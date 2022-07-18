
"""Design an algorithm that creates uniformly random permutations of {0, 1,.. .,fl - 1}. 
You are given a random number generator that returns integers in the set 
10,1, . . . ,n - 7l with equal probability;
use as few calls to it as possible."""
from sampleOnlineData1 import sampleOnlineData


def compute_random_permutation(n):
    permutation = list(range(n))
    sampleOnlineData(permutation, n)
    return permutation


ans = compute_random_permutation(4)
print(ans)
