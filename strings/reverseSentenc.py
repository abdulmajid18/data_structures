sen = "This is a Career Monk String"
# sen = list(sen)

# sen.reverse()
# s = ''.join(sen)
# print(s)


def reverseSen(sen):
    sen = list(sen)
    sen.reverse()
    s = ''.join(sen)
    print(sen)

    def reverse_range(s, start, end):
        while start < end:
            s[start], s[end] = s[end], s[start]
            start, end = start + 1, end - 1
    start = 0
    while True:
        # end = s.find(b'', start)
        end = s.find(" ", start)
        if end < 0:
            break
        reverse_range(sen, start, end-1)
        start = end + 1
    # reverse the last word
    reverse_range(sen, start, len(s)-1)

    return "".join(sen)


# ans = reverseSen(sen)
# print(ans)


x = 'lets pad this sentence'
'senttence this pad lets'

print(x.split())
string_arr = x.split()
elem,max = 0,0
for i in string_arr:
    if len(i) > max:
        max = len(i)
        elem = i
pad_len = len(elem)//2
new = ''
for i in string_arr:
    if i == elem:
        continue
    pad_elem = pad_len*' '
    new += pad_elem+i+pad_elem  
new += elem
print(new)



