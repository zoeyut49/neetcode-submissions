class Solution:
    def isValid(self, s: str) -> bool:
        d = {'(': ')', '{': '}', '[': ']'}
        stk = []
        for i in s:
            if i in d:
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