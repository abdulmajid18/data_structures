# Rotate an array by k position
class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        n = len(nums)
        res = [0] * (n) 
        for i in range(n):
            new_idx = (i + k) % n
            res[new_idx] = nums[i]
        print(res)
            
class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        k = k % len(nums)
        # nums.reverse()
        l, r = 0, len(nums)-1
        while l < r:
            nums[l], nums[r] = nums[r], nums[l]
            l , r = l + 1, r - 1
        
        l, r = 0, k - 1
        while l < r:
            nums[l], nums[r] = nums[r], nums[l]
            l , r = l + 1, r - 1
            
        l, r = k, len(nums) - 1 
        while l < r:
            nums[l], nums[r] = nums[r], nums[l]
            l , r = l + 1, r - 1

class Solution:
    def reverseWords(self, s: str) -> str:
        return " ".join(s.split()[::-1])