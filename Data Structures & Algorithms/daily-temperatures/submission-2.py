class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        stk = []
        i_stk = []
        result = [0]*len(temperatures)
        for i in range(len(temperatures)):
            while stk and temperatures[i] > stk[-1]:
                stk.pop()
                index = i_stk.pop()
                result[index] = i - index
            stk.append(temperatures[i])
            i_stk.append(i)

        return result