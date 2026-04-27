class Solution:
    def minWindow(self, s: str, t: str) -> str:
        dic_t = {}
        for i in t:
            dic_t[i] = dic_t.get(i, 0) + 1
        
        result = ""
        dic_s = {}
        match = 0
        minl = float("inf")
        l = 0
        for r in range(len(s)):
            if s[r] in dic_t:
                dic_s[s[r]] = dic_s.get(s[r], 0) + 1
                if dic_s[s[r]] == dic_t[s[r]]:
                    match += 1
            while match == len(dic_t):
                if (r - l + 1) < minl:
                    result = s[l:r+1]
                    minl = r - l + 1
                if s[l] in dic_t:
                    dic_s[s[l]] -= 1
                    if dic_s[s[l]] < dic_t[s[l]]:
                        match -= 1
                l += 1
        
        return result