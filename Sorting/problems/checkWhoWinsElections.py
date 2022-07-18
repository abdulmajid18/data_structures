A = [3, 2, 1, 2, 2, 3, 3, 3, 3, 3]


def checkWhoWinsWhoElection(A):
    maxi = 0
    for i in range(len(A)):
        counter = 0
        for j in range(len(A)):
            if A[i] == A[j]:
                counter += 1
        if counter > maxi:
            maxi = counter
            element = A[i]
    return element


# ans = checkWhoWinsWhoElection(A)
# print(ans)
A = [3, 2, 1, 2, 2, 3, 3, 3, 3, 3]


def checkWhoWinsWhoElectionSort(A):
    A.sort()
    maxi = 0
    counter = 0
    element = 0
    for i in range(len(A)):
        if A[i] == element:
            counter += 1
        else:
            counter = 1
            element = A[i]
        if counter > maxi:
            maxi = counter
            element = A[i]
    return element


def maxRepititionsWithSort(A):
    A.sort()
    print(A)
    j = 0
    count = max = 1
    element = A[0]
    for i in range(1, len(A)):
        if (A[i] == element):
            count += 1
        if count > max:
            max = count
            maxRepeatedElement = element
        else:
            count = 1
            element = A[i]
    print(maxRepeatedElement, "repeated for ", max)


A = [3, 2, 1, 3, 2, 3, 2, 3, 3]
maxRepititionsWithSort(A)


ans = checkWhoWinsWhoElectionSort(A)
print(ans)
