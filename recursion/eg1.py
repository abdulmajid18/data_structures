

x = [1, 3, 5, 7, 9]


def list_sum(nums):
    the_sum = 0
    for i in nums:
        the_sum += i
    return the_sum

# ans = list_sum(x)
# print(ans)


def list_sum_recurse(nums):
    if len(nums) == 1:
        return nums[0]
    if len(nums) == 0:
        return 0
    else:
        return nums[1] + nums[0] + list_sum_recurse(nums[2:])


# def list_sum(num_list):
#     if len(num_list) == 1:
#         return num_list[0]
#     else:
#         return num_list[0] + list_sum(num_list[1:])
#     # print(list_sum([1,3,5,7,9]))


# ans = list_sum_recurse(x)
# print(ans)
print(10//10)
print(10 % 10)


def convert_int_to_str(num, base):
    convert_str = "0123456789ABCDEF"
    if num < base:
        return convert_str[num]
    else:
        return convert_int_to_str(num // base, base) + convert_str[num % base]


print(convert_int_to_str(10, 2))
