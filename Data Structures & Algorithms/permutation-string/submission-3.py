class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        if len(s1) > len(s2):
            return False
        
        dic1 = {}
        for s in s1:
            dic1[s] = 1 + dic1.get(s, 0)
        
        k = len(s1)
        dic2 = {}
        for j in range(k):
            dic2[s2[j]] = 1 + dic2.get(s2[j], 0)
        if dic2 == dic1:
            return True

        for r in range(k, len(s2)):
            dic2[s2[r]] = 1 + dic2.get(s2[r], 0)
            dic2[s2[r - k]] -= 1
            if dic2[s2[r - k]] == 0:
                del dic2[s2[r - k]]
            
            if dic2 == dic1:
                return True
        
        return False