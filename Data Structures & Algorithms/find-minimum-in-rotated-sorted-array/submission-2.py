class Solution:
    def findMin(self, nums: List[int]) -> int:
        l, r = 0, len(nums) - 1
        minn = 1001
        
        while l <= r:
            mid = (l + r) // 2
            minn = min(minn, nums[mid])

            if nums[mid] > nums[r]:
                l = mid + 1
            else:
                r = mid - 1


        return minn
