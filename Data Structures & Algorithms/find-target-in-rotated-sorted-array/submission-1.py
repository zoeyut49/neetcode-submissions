class Solution:
    def search(self, nums: List[int], target: int) -> int:
        l = 0
        r = len(nums) - 1
        while l <= r:
            index = (l + r) // 2
            if nums[index] == target:
                return index
            if nums[index] <= nums[r]:
                if nums[index] > target or nums[r] < target:
                    r = index - 1
                else:
                    l = index + 1
            else:
                if nums[index] < target or nums[l] > target:
                    l = index + 1
                else:
                    r = index - 1
        
        return -1