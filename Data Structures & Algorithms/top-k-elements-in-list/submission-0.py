class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        d = {}
        for num in nums:
            if num in d.keys():
                d[num] += 1
            else:
                d[num] = 0

        res = []
        for key, value in d.items():
            res.append([key,value])
        res = sorted(res, key=lambda x: x[1])

        result = []
        for i in range(k):
            result.append(res[len(res) - 1 - i][0])

        return result