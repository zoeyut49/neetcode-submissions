class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        l = 0
        maxl = 0
        count = {}
        for r in range(l, len(s)):
            if s[r] in count:
                count[s[r]] += 1
            else:
                count[s[r]] = 1
            while r - l + 1 - max(count.values()) > k:
                count[s[l]] -= 1
                l += 1
            maxl = max(maxl, r - l + 1)
        return maxl