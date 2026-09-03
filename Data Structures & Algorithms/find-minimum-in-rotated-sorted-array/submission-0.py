class Solution:
    def findMin(self, nums: List[int]) -> int:
        minn = 1001
        
        for n in nums:
            minn = min(minn, n)

        return minn
