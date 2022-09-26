A = [2,1,1,2]

def rob(self, nums) -> int:
    max_sum = 0
    current_sum = 0
    for i in range(0, len(nums), 2):
        current_sum += nums[i]
        max_sum = max(max_sum, current_sum)
    current_sum = 0
    for j in range(1, len(nums),2):
        current_sum += nums[j]
        max_sum = max(max_sum, current_sum)
    return max_sum
A = [183,219,57,193,94,233,202,154,65,240,97,234,100,249,186,66,90,238,168,128,177,235,50,81,185,165,217,207,88,80,112,78,135,62,228,247,211]

def rob(nums, table={}) -> int:
    key = ''.join([str(s) for s in nums])
    if key in table:
        return table[key]
    if len(nums) == 1:
        return nums[0]
    if len(nums) == 2:
        ans = max(nums[0], nums[-1])
        return ans
    table[key] =  max(nums[0]+ rob(nums[2:len(nums)], table), rob(nums[1:], table))
    print(table)
    return table[key]

# ans = rob(A)
# print(ans)
class Solution:
    # table = {}
    def rob(self, nums, table={}) -> int:
        key = ''.join([str(s) for s in nums])
        if key in table:
            return table[key]
        if len(nums) == 1:
            return nums[0]
        if len(nums) == 2:
            ans = max(nums[0], nums[-1])
            return ans
        table[key] =  max(nums[0]+ self.rob(nums[2:len(nums)], table), self.rob(nums[1:], table))
        print(table)
        return table[key]

inst = Solution()
inst.rob(nums=A)