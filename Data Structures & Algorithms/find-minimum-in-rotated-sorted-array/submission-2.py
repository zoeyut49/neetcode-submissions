class Solution:
    def findMin(self, nums: List[int]) -> int:
        i = 0
        j = len(nums) - 1
        res = nums[0]
        if nums[0] < nums[-1]:
            return nums[0]
        while i <= j:
            index = (i + j) // 2
            if nums[index] > nums[j]:
                res = min(res, nums[j])
                i = index + 1
            elif nums[index] <= nums[j]:
                res = min(res, nums[index])
                j = index - 1
        
        return res