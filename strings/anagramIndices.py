from collections import Counter, defaultdict
def anagrm_indices(w,s):
    result = []
    w_size = len(w)
    for i in range(len(s)-1):
        word = s[i : i+w_size]
        if Counter(w) == Counter(word):
            result.append(i)
        # You can remove the else statementt to mitigate noise
        else:
            continue
    print(result)

        
# anagrm_indices('ab', 'abxaba')
from collections import Counter
def is_anagram(s1, s2):
    return Counter(s1) == Counter(s2)
def anagram_indices(word, s):
    result = []
    for i in range(len(s) - len(word) + 1):
        window= s[i:i+len(word)]
        if is_anagram(window, word):
            result.append(i)
    return result



def del_if_zero(dict, char):
    if dict[char] == 0:
        del dict[char]

def anagram_indices(word, s):
    result = []

    freq = defaultdict(int)

    for char in word:
        freq[char] += 1

    for char in s[:len(word)]:
        freq[char] -= 1
        del_if_zero(freq, char)
    
    if not freq:
        result.append(0)
    
    for i in range(len(word), len(s)):
        start_char, end_char = s[i-len(word)], s[i]
        freq[start_char] += 1
        del_if_zero(freq, start_char)

        freq[end_char] -= 1



anagram_indices('ab', 'abxaba')

    

