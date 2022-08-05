
x = 'akchebfj'

new = x[1:] + x[:1]
print(new)
new = new[:1] + new[2:] + new[1:2]
new = new[1:] + new[:1]
print(new)