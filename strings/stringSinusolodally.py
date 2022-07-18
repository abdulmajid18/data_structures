s = 'Hello_world'

# print(s[1::4])
# print(s[::2])
# print(s[3::4])

# Pythonic solution using slicing


def snake_string_pythonic(s):
    return s[1::4] + s[::2] + s[3::4]


def snake_string(s):
    result = []
    for i in range(1, len(s), 4):
        result.append(s[i])
    for i in range(0, len(s), 2):
        result.append(s[i])
    for i in range(3, len(s), 4):
        result.append(s[i])
    return ''.join(result)
