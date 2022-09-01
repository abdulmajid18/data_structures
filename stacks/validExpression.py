A = "{{([][])}()}"
B = "()(()[()])"


def isValidExpression(expression):
    mappings = {')': '(', ']': '[', '}': '{'}
    stack = []
    for string in expression:
        if string in mappings:
            element = stack.pop() if stack else '#'
            if mappings[string] != element:
                return False
        else:
            stack.append(string)
    return not stack


C = "([)]"
# print(isValidExpression(B))


def isValid(self, s: str) -> bool:
    parentheses = {'(': ')', '{': '}', '[': ']'}
    stack = []
    for b in s:  # take bracket 'b' from string 's'
        if b in parentheses:  # if bracket in parentheses
            stack.append(parentheses[b])  # append it's opposite to stack
        elif not stack or stack.pop() != b:  # if not stack or bracket not
            return False                    # equal last bracket in stack
    return not stack  # if stack still exists -> False else True


#     def isValid(self, s: str) -> bool:
#         if len(s) % 2 != 0:
#             return False
#         dict = {'(': ')', '[': ']', '{': '}'}
#         stack = []
#         for i in s:
#             if i in dict.keys():
#                 stack.append(i)
#             else:
#                 if stack == []:
#                     return False
#                 a = stack.pop()
#                 if i != dict[a]:
#                     return False
#         return stack == []
# #
A = "{{([][])}()}"
B = "()(()[()])"

def is_well_informed(s):
    left_chars, lookup = [], {'(': ')', '{': '}', '[': ']'}
    for c in s:
        if c in lookup:
            left_chars.append(c)
        elif not left_chars or lookup[left_chars.pop] != c:
            return False
    return not left_chars