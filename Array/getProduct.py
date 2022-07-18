from functools import reduce
import re
""" Get the product of al other elements"""

def get_product_brute(A):
    """Given an array of Integer, return a new array such that 
    each element at index i of the new aray is he product of 
    all the numbers in the original except the one at i"""

    # A = [1,2,3,4,5]

    new_arr = []
    for i,_ in enumerate(A):
        cur_val = 1
        for j,v2 in enumerate(A):
            if i == j:
                continue
            cur_val *= v2
        new_arr.append(cur_val)
    print(new_arr)

def get_product_division(A:list):
    """Since division is opposite for mltiplication
    We can multiply all elements and divide the unwanted part ie the element too ignore ):"""
    result = reduce((lambda x, y: x * y), A)
    for i,v in enumerate(A):
        sum = result // v
        A[i] = sum
    print(A)

A = [1,2,3,4,5]
# A = [3,2,1]


def products(nums):
    # Generate prefix
    prefix_products = []
    for v in nums:
        if prefix_products:
            prefix_products.append(prefix_products[-1] * v)
        else:
            prefix_products.append(v)
            
    suffix_product = []
    for v in reversed(nums):
        if suffix_product:
            suffix_product.append(suffix_product[-1] * v)
        else:
            suffix_product.append(v)
    suffix_product = list(reversed(suffix_product))
    print(prefix_products)
    print(suffix_product)
    for i,v in enumerate(nums):
        if i == 0:
            nums[i] = v
        elif i == len(A) - 1:
            nums[i] = prefix_products[-1]
        else:
            prefix = prefix_products[i-1]
            sufix = suffix_product[i+1]
            nums[i] = prefix * sufix
    print(nums)





products(A)




# get_product_division(A)

