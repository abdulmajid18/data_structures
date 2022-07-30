from collections import defaultdict

x = ["debitcard", "elvis", "silent", 'badcredit', 'lives', 'freedom',
"listen","levis","money"]

def find_anagram(dictionary):
    sorted_string_to_anagrams = defaultdict(list)
    for s in dictionary:
        sorted_string_to_anagrams[''.join(sorted(s))].append(s)

    return [
    group for group in sorted_string_to_anagrams.values() if len(group) >= 2
    ]

ans = find_anagram(x)

"""A palindrome is a string that can reas the same forwards  
and backwards eg level , rotator and foobaraboof"""
from collections import Counter
def check_palindrome_permutation(s):
    palindrome_count = [ v for v in Counter(s).values()]
    check_odd = [ v % 2 for v in palindrome_count]
    odd_sum = sum(check_odd) <= 1
    print(odd_sum)

check_palindrome_permutation("rotator")
print(Counter("rotator"))



























