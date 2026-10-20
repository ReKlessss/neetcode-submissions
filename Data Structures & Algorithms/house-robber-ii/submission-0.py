class Solution:
    def rob(self, nums: List[int]) -> int:
        if len(nums) == 1: return nums[0]

        memo = [[-1] * 2 for _ in range(len(nums))]

        def dfs(i: int, first_robbed: bool) -> int:
            if i >= len(nums) or (first_robbed and i == len(nums) - 1):
                return 0

            if memo[i][first_robbed] != -1:
                return memo[i][first_robbed]

            memo[i][first_robbed] = max(dfs(i + 1, first_robbed), 
                                        nums[i] + dfs(i + 2, first_robbed or (i == 0)))

            return memo[i][first_robbed]

        return max(dfs(0, True), dfs(1, False))