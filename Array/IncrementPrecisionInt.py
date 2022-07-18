"""
Write a program that takes an input as a array of digits encoding
a non negative decimal integer D and updates the array to 
Integer D+1. Eg [1,2,9]  --> [1,3,0]
"""


def plus_one(A):
    """
    A Brute force implemenation is to convert te array to an int
    And add the increental value to it after which it is then converted 
    to an array
    """
    x = [f'{i}' for i in A]
    print(x)
    int_a = int(''.join(x))
    print(int_a)
    ans = str(int_a + 1)
    print(ans)
    ans = [i for i in ans]
    return ans


# x = plus_one([1, 2, 9])
# print(x)

def plus_one_impl(A):
    A[-1] += 1
    for i in reversed(range(1, len(A))):
        # 2,1
        if A[i] != 10:
            break
        A[i] = 0
        A[i-1] += 1

    if A[0] == 10:
        A[0] = 1
        A.append(0)

    return A


x = plus_one_impl([1, 2, 9])
print(x)
