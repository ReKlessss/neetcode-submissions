class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        res = []

        visited = set()
        seq = []
        def dfs():
            if len(seq) == len(nums):
                res.append(seq.copy())
                return

            for n in nums:
                if n in visited: continue

                seq.append(n)
                visited.add(n)
                
                dfs()
                
                seq.pop()
                visited.remove(n)
        
        dfs()
        return res