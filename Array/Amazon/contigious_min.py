processes = [10, 4, 8, 13, 20]

m = 2

def delete_servers(arr, m):
    max_sum = 0
    idx = 0
    for i in range(0,len(arr)-m+1, 1):
        new_sum = sum(arr[i:i+m])
        if new_sum > max_sum:
            max_sum = max(max_sum, new_sum)
            idx = i
    del arr[idx:idx+m]
    print(sum(arr))

delete_servers(processes,m)



movies = [1,5,4,6,8,9,2]
k = 3
def movie_group(movies, k):
    for i in movies:
        pass




        