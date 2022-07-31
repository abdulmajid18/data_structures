from collections import Counter


"""Generate palindrome pairs
Given a list of words, find all the pairs of unique
Indices such that the concatenation of the words is a 
palindrome
"""

def is_palindrome(s):
    # i noves forward, and j noves backward.
    s = [x for x in str(s)]
    i, j = 0, len(s)-1

    while i < j:
        # i and j both skip non-alphanuneric characters
        if s[i].lower() != s[j].lower():
            return False
        i, j = i + 1, j - 1
    return True

def is_palindrome_2(word):
    return word == word[::1]

from collections import Counter

x  = ["code", "edoc", "da", "d"]
def palindrome_pairs(words):
    result = []
    for i,v in enumerate(x):
        for j,v2 in enumerate(x):
            if i == j:
                continue
            new_string = v + v2
            if is_palindrome(new_string):
                result.append((i,j))
    print(result)
table = {}
for i, v in enumerate(x):
    table[v] = i
results = []

for i, word in enumerate(x):
    for char_i in range(len(word)):
        prefix, suffix = word[:char_i],  word[char_i:]
        reversed_prefix = prefix[::-1]
        reversed_suffix = suffix[::-1]
        # print(reversed_prefix, reversed_suffix)
        
        if is_palindrome(suffix):
            pass
# Te above to be continued

"""Write a program which takes text for an anonymous letter and text for a rnagazine and determines
if it is possible to write the anonymous letter using the magazine. The anonymous letter can be
written using the magazine if for each character in the anonymous letter, the number of times it
appears in the anonymous letter is no more than the number of times it appears in the magazine."""


x = 'majidnuhu'
y = 'nuhuamjid'
def hash_chars(strings):
    hash_table = {}
    for i in x:
        if i in hash_table:
            hash_table[i] += 1
        else:
            hash_table[i] = 1
    return hash_table


def count_char(strings, element):
    count = 0
    for i in strings:
        if element == i:
            count += 1 
    return count
def is_letter_from_magazine(x, y):
    for i in x:
        element = i
        count = count_char(x, element)
        for j in y:
            count_2 = count_char(y, element)
        if count == count_2:
            continue
        else:
            return False
    return True

def is_letter_consructible_from_magazine(letter_text, magazine_letter):
    hash_table = hash_chars(letter_text)
    for i in magazine_letter:
        if i in hash_table:
            hash_table[i] -= 1
        else:
            return False
    count = 0
    for i in hash_table:
        count += hash_table[i]
    if count == 0:
        return True
    else:
        return False
        
def is_leter_constructible_from_magazine_2(letter, magazine):
    char_frquency_for_letter = Counter(letter)

    for c in magazine:
        if c in char_frquency_for_letter:
            char_frquency_for_letter[c] -= 1
            if char_frquency_for_letter[c] == 0:
                del char_frquency_for_letter[c]
                if not char_frquency_for_letter:
                    return True
    return not char_frquency_for_letter


def is_leter_constructible_from_magazine_pythonic(letter, magazine):
    return not  Counter(letter) - Counter(magazine)
    
ans = is_leter_constructible_from_magazine_pythonic(x, y)

    
    
