class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        res = [0] * len(temperatures)
        s = []

        for i, temp in enumerate(temperatures):
            while s and temperatures[s[-1]] < temp:
                prev_idx = s.pop()
                res[prev_idx] = i - prev_idx
            
            s.append(i)

        return res