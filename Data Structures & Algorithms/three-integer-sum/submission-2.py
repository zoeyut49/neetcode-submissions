class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        results = []

        for n in range(len(nums)):
            if nums[n] > 0:
                break

            if n > 0 and nums[n] == nums[n-1]:
                continue
            
            i = n + 1
            j = len(nums) - 1
            while i < j:
                threesum = nums[n] + nums[i] + nums[j]
                if threesum > 0:
                    j -= 1
                elif threesum < 0:
                    i += 1
                else:
                    results.append([nums[n], nums[i], nums[j]])
                    i += 1
                    j -= 1
                    while nums[i] == nums[i-1] and i < j:
                        i += 1
                 
        return results