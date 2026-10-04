class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        nums = sorted(nums)
        res = []


        curr = []
        def dfs(i: int):
            if i >= len(nums):      
                res.append(curr.copy())
                return

            curr.append(nums[i])
            dfs(i + 1)

            while i < len(nums) and nums[i] == curr[-1]:
                i += 1

            curr.pop()
            dfs(i)

        dfs(0)
        return res