""" Writte a program that takes as input an array and finds the distance
Between a closest pair of equal entries"""

s = ['All', 'work', 'and', 'no', 'play', 'makes','for', 'work', 'no',
'fun', 'and', 'no', 'results']

from collections import namedtuple
Distance = namedtuple("Distance", ("min", "max"))
# def get_distance(i,j):
#     return Distance(d)
# prev = Distance
def solu(s):
    prev = Distance(0, 0)
    for i,v in enumerate(s):
        for j,v1 in enumerate(s):
            if  i != j and v == v1:
                prev_dif = prev.max - prev.min
                if j > i:
                    cur = Distance(i,j)
                    cur_dif = cur.max - cur.min
                    if cur_dif < prev_dif:
                        prev = Distance(i,j)
                        ans = prev
                    print(i,j,v)
                    i = j 
    print(ans.min, ans.max)

solu(s)


def find_nearest_repetition(paragraph):
    word_to_latest, nearest_repeated_distance =  {}, float('inf')
    for i, word in enumerate(paragraph):
        if word in word_to_latest:
            lastest_equal_word = word_to_latest[word]
            nearest_repeated_distance = min(nearest_repeated_distance, i - lastest_equal_word)
        word_to_latest[word] = i
            
    return nearest_repeated_distance if nearest_repeated_distance != float('inf') else -1
    
            
        



    
    

