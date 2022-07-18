# result = [0, 1, 1, 0, 0, 2, 0]

# y = (i for i, x in enumerate(result) if x != 0)

# print(y)

# z = result[next(y, len(result)):]

# print(z)


# result = result[next((i for i, x in enumerate(result)
#                       if x != 0), len(result)):] or [0]
# print(result)

x = [1, 2, 3]
y = [9]
print(x+y)
