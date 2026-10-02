class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        candidates = sorted(candidates)
        res = []

        curr = []
        def dfs(i: int, total: int): 
            if total == target:
                res.append(curr.copy())
                return

            if i >= len(candidates) or total > target:
                return
            
            curr.append(candidates[i])
            dfs(i + 1, total + candidates[i])

            while i < len(candidates) and candidates[i] == curr[-1]:
                i += 1    

            curr.pop()
            dfs(i, total)

        dfs(0, 0)
        return res
