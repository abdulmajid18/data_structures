"I,V,X,L,C,D,M"
from functools import reduce


def roman_to_int(s):
    T = {"I": 1, "V": 5, "X": 10, "L": 50, "C": 500, "D": 100, "M": 1000}
    return reduce(lambda val, i: val + (-T[s[i]] if T[s[i]] < T[s[i+1]]
                                        else T[s[i]]), reversed(range(len(s)-1)), T[s[-1]])


x = "LIX"
ans = roman_to_int(x)
print(ans)
