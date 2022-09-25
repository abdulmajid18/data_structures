"""Given an array of numbers, :find the maximum sum of any contiguous subarray of
the array. For example, given the array [34, -50, 42, 14, -5, 86], the maximum
sum would be 137, since we would take elements 42, 14, -5, and 86. Given the array
[ -5, -1, -8, -9], the maximum sum would be 0, since we would choose not to
take any elements."""

x = [34, -50, 42, 14, -5, 86]
# x = [ -5, -1, -8, -9]

actual_sum = 0
for i in range(len(x)-1):
    for j in range(i, len(x)):
        new_cur = sum(x[i:j])
        actual_sum = max(actual_sum, new_cur)

print(actual_sum)
def max_subarray_sum(arr):
    current_max = 0
    for i in range(len(arr) - 1):
        for j in range(i, len(arr)):
            current_max = max(current_max, sum(arr[i:j]))
    return current_max


def max_subarray_dp(arr):
    max_here = max_so_far = 0
    for x in arr:
        max_here = max(x, max_here+x)
        max_so_far = max(max_so_far, max_here)
    return max_so_far

ans = max_subarray_dp(x)
print(ans)
ans = max_subarray_sum(x)
print(ans)