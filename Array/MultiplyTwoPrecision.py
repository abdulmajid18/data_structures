"""
The code below iis  foor utipling ony two positive first character array
"""


def multiply_precision(A, B):
    a = [f"{a}" for a in A]
    b = [f"{b}" for b in B]
    a = int("".join(a))
    b = int("".join(b))
    ans = a * b
    ans = [f'{i}' for i in str(ans)]
    return ans


# print(multiply_precision([1, 2], [1, 2]))
num1 = [1, 2, 2]
num2 = [1, 2, 2]

# sign = -1 if (num1[0] < 0) ^ (num2[0] < 0) else 1
# num1[0], num2[0] = abs(num1[0]), abs(num1[1])
# result = [0] * (len(num1)+len(num2))
# for i in reversed(range(len(num1))):
#     # [2,1,0]
#     for j in reversed(range(len(num2))):
#         # [2,1,0]
#         result[] += num1[i] * num2[j]
# print(sign)


def multiply(num1, num2):
    sign = -1 if (num1[0] < 0) ^ (num2[0] < 0) else 1
    num1[0], num2[0] = abs(num1[0]), abs(num2[0])

    result = [0] * (len(num1) + len(num2))
    for i in reversed(range(len(num1))):
        for j in reversed(range(len(num2))):
            result[i+j+1] += num1[i] * num2[j]
            result[i+j] += result[i+j+1] // 10
            result[i+j+1] %= 10
    #  Remove the leading zeros

    result = result[next((i for i, x in enumerate(result)
                          if x != 0), len(result)):] or [0]
    return [sign * result[0]] + result[1:]


print(multiply([1, 2, 3], [9, 8, 7]))
