def UnOrderedSearch(elements: list, element):
    for i in elements:
        if i == element:
            return elements.index(element)
    return -1


def UnOrdereSearch_2(elements, element):
    for i in range(len(elements)):
        if elements[i] == element:
            return i
    return -1


def UnOrderedSearh_3(elements, element):
    for i, v in enumerate(elements):
        if v == element:
            return i
    return -1


A = [534, 246, 933, 127, 277, 321, 454, 565, 220]

print(UnOrderedSearch(A, 246))
print(UnOrdereSearch_2(A, 246))
print(UnOrderedSearh_3(A, 246))
