#  integer n first line
N = int(input())
#  len of array is N in the fisrt line
arr = input().split(" ")

print(f"N is  {N} and Array is {arr}")

table = {}
for element in arr:
    table[element] = table.get(element,0)+1
maxi = 0
maxi_element = 0
for element in arr:
    if table[element] > maxi:
        maxi = table[element]
        maxi_element = element
    if table[element] == maxi:
        if maxi_element < element:
            maxi_element = element 
print(table)
print(f"Maximun occurece is {maxi} by number {maxi_element}")

