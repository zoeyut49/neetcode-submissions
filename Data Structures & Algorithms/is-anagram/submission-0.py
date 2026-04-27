class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        dic_s = dict()
        dic_t = dict()

        for i in s:
            if i in dic_s.keys():
                dic_s[i] +=1
            else:
                dic_s[i] = 0

        for i in t:
            if i in dic_t.keys():
                dic_t[i] +=1
            else:
                dic_t[i] = 0
        
        if dic_s == dic_t:
            return True
        else:
            return False