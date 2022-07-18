def OrderedLinearSearch(elements, element):
    for i, v in enumerate(elements):
        if v == element:
            return i
        elif v > element:
            return -1
    return -1


A = [34, 46, 93, 127, 277, 321, 454, 565, 1220]
print(OrderedLinearSearch(A, 5655))
