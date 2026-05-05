class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        res = [0] * len(temperatures)
        stack = []

        for t in range(len(temperatures)-1, -1, -1):
            while stack and stack[-1][0] <= temperatures[t]:
                stack.pop()

            if stack:
                res[t] = stack[-1][1] - t
            stack.append([temperatures[t], t])
        return res        

        
        