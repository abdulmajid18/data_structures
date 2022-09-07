from collections import Counter
A = [('Ian','Bell'), ('David', 'Gower'), 
('Ian','Botham'), ('Ian', 'Chappen')]

"""Remove first name duplicate"""
table = {}
for name in A:
    if name[0] in table:
        old_name = table[name[0]]
        table[name[0]] = old_name
    elif name[0] != "":
        table[name[0]] = name
    else:
        table[name[0]] = 0
# print([ans for ans in table.values()])

def eliminate_duplicate(A):
    A.sort()
    write_idx = 1
    for cand in A[1:]:
        if cand != A[write_idx-1]:
            A[write_idx] = cand
            write_idx += 1
    del A[write_idx:]
    print(A)
def removeDuplicateSort(A):
    A.sort()
    j = 0
    for i in range(1, len(A)):
        if (A[j] != A[i]):
            j += 1
            A[j] = A[i]
    print(A[:j+1])
A= [1,1,2,4,5,6,1,4]
A = [1,1,1,2,4,4,5,6]
eliminate_duplicate(A)