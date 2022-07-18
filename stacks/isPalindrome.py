from postfixInfixConversion import Stack


def isPalindrome(A):
    i = 0
    j = len(A)-1
    flag = False
    while i <= j:
        if A[i] == A[j]:
            flag = True
        else:
            flag = False
            return False
        i += 1
        j -= 1
    if not flag:
        return False
    else:
        return True


def isPalindromeB(A):
    i = 0
    j = len(A) - 1

    while i < j and A[i] == A[j]:
        i += 1
        j -= 1
    if (i < j):
        print("Not a Palindrome")
        return 0
    else:
        print("Palindrome")
    return 1


def isPalindromeA(str):
    strStack = Stack()
    palindrome = False
    for char in str:
        strStack.push(char)
    for char in str:
        if char == strStack.pop():
            palindrome = True
        else:
            palindrome = False
            return False
    return palindrome


A = ['m', 'a', 'd', 'a', 'm']
ans = isPalindromeA(A)
print(ans)
