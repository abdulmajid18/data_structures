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


# x = is_palindrome(100)

x = "Abdul"
print(id(x))
y = "Majid"
x += "Majid"
print(id(x))
