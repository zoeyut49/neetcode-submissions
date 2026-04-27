class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        mul = 1
        zero = False
        for n in nums:
            if zero == False and n == 0:
                zero = True
                continue
            mul = mul * n
        
        result = []
        for i in nums:
            if zero == True and i != 0:
                result.append(0)
            elif zero == True and i == 0:
                result.append(mul)
            else:
                result.append(mul//i)
        
        return result