class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        res = {j: 0 for j in range(len(temperatures))}
        s = []

        for i, temp in enumerate(temperatures):
            while s and s[-1][0] < temp:
                temp_tuple = s.pop()
                res[temp_tuple[1]] = i - temp_tuple[1]
            
            s.append((temp, i))

        return list(res.values())