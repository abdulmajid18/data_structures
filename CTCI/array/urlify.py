from collections import Counter
s = "Mr John Smith"

def urlifyBrute(s):
    new = list(s)
    for i in range(len(new)-1):
        if new[i] == ' ' :
            new[i] = "%20"
    char = "".join(new)
    print(char)

urlifyBrute(s)

def urlify_concatenate(string, true_length):
    """
    This solution traverse through original string and 
    create a new string by appending characters if it is space then,
    it appends "%20".

    Time Complexity: O(n^2), because string is immutable
    Space Complexity: O(n)
    """

    result_string = ""
    for i in range(true_length):
        if string[i] == " ":
            result_string += "%20"
        else:
            result_string += string[i]
    return result_string




def urlify_list(string, true_length):
    """
    This solution converts the sting into list and then 
    edits the string in backward direction by replacing 
    space with "%20".

    Time Complexity: O(n)
    Space Complexity: O(n)
    """

    char_list = list(string)
    index = len(string)
    for i in range(true_length - 1, -1, -1):
        if string[i] == " ":
            char_list[index - 1] = "0"
            char_list[index - 2] = "2"
            char_list[index - 3] = "%"
            index -= 3
        else:
            char_list[index - 1] = string[i]
            index -= 1
    return "".join(char_list)


def urlify(s, i):
    p1, p2 = len(s) - 1, i - 1
    while p1 >= 0 and p2 >= 0:
        if s[p2] != " ":
            s[p1] = s[p2]
            p1 -= 1
            p2 -= 1
        else:
            for i in reversed("%20"):
                s[p1] = i
                p1 -= 1
            p2 -= 1


def is_palindrome_permutation(string):
  counter = Counter()
  for letter in string.replace(" ", ""):
    counter[letter] += 1
  #return sum([count % 2 for count in counter.values()]) < 2
  odd_counts = 0
  for count in counter.values():
    odd_counts += count % 2
    if odd_counts > 1:
      return False
  return True