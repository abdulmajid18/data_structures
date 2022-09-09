class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        nums.sort()
        nums.reverse()
        return nums[k-1]
class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        k = len(nums)-k
        def quick_select(start, stop):
            pivot_value = nums[stop]
            pivot_index = start
            for i in range(start, stop):
                if nums[i] <= pivot_value:
                    nums[i], nums[pivot_index] = nums[pivot_index], nums[i]
                    pivot_index += 1
            nums[stop], nums[pivot_index] = nums[pivot_index], nums[stop]
            
            if pivot_index > k:
                return quick_select(start, pivot_index-1)
            elif pivot_index < k:
                return quick_select(pivot_index+1, stop)
            else:
                return nums[pivot_index]
        
        return quick_select(0, len(nums)-1)