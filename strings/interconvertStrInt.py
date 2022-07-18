import functools
import string


def convert_int_to_str(num, base):
    convert_str = "0123456789ABCDEF"
    if num < base:
        return convert_str[num]
    else:
        return convert_int_to_str(num // base, base) + convert_str[num % base]


print(convert_int_to_str(615, 13))
# print(9 // 10)
# x = 11
# print(chr(49))
# print(chr(ord('0') + x % 10))


def int_to_str(x):
    is_negative = False
    if x < 0:
        x, is_negative = -x, True
    s = []
    while True:
        s.append(chr(ord('0') + x % 10))
        x //= 10
        if x == 0:
            break

    return ('-' if is_negative else '') + ''.join(reversed(s))


ans = int_to_str(98)
# print(ans)

# s = 314


def string_to_int(s):
    return functools.reduce(lambda running_sum, c: running_sum * 10 + string.digits.index(c),
                            s[s[0] == '-':], 0) * (-1 if s[0] == '-' else 1)


# x = '-869'
# print(x[0] == '-')
# print(x[x[0] == '-':])
# print(x[True:])
# ans = string_to_int('985')
# print(ans)
