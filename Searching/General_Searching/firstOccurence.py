x = [2,4,5,5,5,5,5,7,9,9]
elem = 5
def find_first_occurence(x, elem=5):
    n = len(x)
    left = 0
    right = n-1
    lastfound = 0
    while True:
        if left > right:
            return lastfound
        mid = (left + right) // 2
        if x[mid] == elem:
            lastfound = mid
            right = mid - 1
        if x[mid] > elem:
            right = mid - 1
        if x[mid] < elem:
            left = left + 1

ans = find_first_occurence(x)
print(ans)