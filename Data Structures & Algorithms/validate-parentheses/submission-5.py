class Solution:
    def isValid(self, s: str) -> bool:
        d = {'(': ')', '{': '}', '[': ']'}
        stk = []
        if len(s) == 1:
            return False
        for i in s:
            if i in d.keys():
                stk.append(i)
            else:
                if stk and i == d[stk[-1]]:
                    stk.pop()
                else:
                    return False
        if stk:
            return False
        else:
            return True