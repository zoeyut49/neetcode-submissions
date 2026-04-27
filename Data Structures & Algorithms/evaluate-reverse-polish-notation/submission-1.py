class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stk = []
        for n in tokens:
            if n != '+' and n != '-' and n != '*' and n != '/':
                stk.append(int(n))
            else:
                val2 = stk.pop()
                val1 = stk.pop()
                if n == '+':
                    val = val1 + val2
                elif n == '-':
                    val = val1 - val2
                elif n == '*':
                    val = val1 * val2
                elif n == '/':
                    val = int(val1 / val2)
                stk.append(val)
        return stk.pop()