class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        
        if len(s) != len(t):
            return False
        
        dic_s = dict()
        dic_t = dict()

        for i in range(len(s)):
            if s[i] in dic_s.keys():
                dic_s[s[i]] += 1
            else:
                dic_s[s[i]] = 0

            if t[i] in dic_t.keys():
                dic_t[t[i]] += 1
            else:
                dic_t[t[i]] = 0
        
        if dic_s == dic_t:
            return True
        else:
            return False