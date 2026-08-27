class Solution:
    def search(self, nums: List[int], target: int) -> int:
        l = 0
        h = len(nums) - 1

        while l <= h:
            m = (l + h) // 2
            guess = nums[m]
            
            if guess > target:
                h = m - 1
            elif guess < target:
                l = m + 1
            else:
                return m

        return -1