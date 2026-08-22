class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        if len(nums) <= 1: return False
        
        nums_set = set(nums)

        if len(nums_set) == len(nums):
            return False

        return True