x = [1,10,48,5,3,74,25,14,23,85,14,56,3]

x.sort()
print(f"The first sort {x}")

new = reversed(x)
print(f"The new sorted function {new}")

new = [new for new in new]
print(f"The new two sorted function {new}")