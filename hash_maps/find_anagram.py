from collections import defaultdict

def find_anagram(dictionary):
    sorted_string_to_anagrams = defaultdict(list)
    for s in dictionary:
        sorted_string_to_anagrams[''.join(sorted(s))].append(s)

    return [
    group for group in sorted_string_to_anagrams.values() if len(group) >= 2
    ]

