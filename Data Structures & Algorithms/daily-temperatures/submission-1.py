class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        stk = [temperatures[0]]
        i_stk = [0]
        result = [0]*len(temperatures)
        for i in range(1,len(temperatures)):
            while stk and temperatures[i] > stk[-1]:
                stk.pop()
                index = i_stk.pop()
                result[index] = i - index
            stk.append(temperatures[i])
            i_stk.append(i)
        while stk:
            value = stk.pop()
            index = i_stk.pop()
            result[index] = 0
        return result