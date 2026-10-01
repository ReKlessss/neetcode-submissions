class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        res = []

        seq = []
        def dfs(i: int, total: int):
            if total == target:
                res.append(seq.copy())
                return

            if i >= len(nums) or total > target:
                return

            seq.append(nums[i])
            dfs(i, total + nums[i])

            seq.pop()
            dfs(i + 1, total)

        dfs(0, 0)
        return res