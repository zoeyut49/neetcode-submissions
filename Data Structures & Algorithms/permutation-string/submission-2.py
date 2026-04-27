class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        dic1 = {}
        for s in s1:
            if s in dic1:
                dic1[s] += 1
            else: 
                dic1[s] = 1
        n1 = len(s1)
        i = 0
        while i + n1 <= len(s2):
            dic2 = {}
            for j in range(i, i + n1):
                if s2[j] in dic2:
                    dic2[s2[j]] += 1
                else: 
                    dic2[s2[j]] = 1
            if dic2 == dic1:
                return True
            i += 1
        return False