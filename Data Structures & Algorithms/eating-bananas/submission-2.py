class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        l = 1
        r = max(piles)
        while l <= r:
            index = (l + r) // 2
            hour = 0
            for p in piles:
                hour += math.ceil(p / index)
            if hour > h:
                l = index + 1
            else:
                res = index
                r = index - 1
        return res
        