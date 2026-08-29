class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        output = []
        left = [1] * len(nums)
        right = [1] * len(nums)

        for i in range(1, len(nums)):
            ans = left[i - 1] * nums[i - 1]
            left[i] = ans

        for i in range(len(nums) - 2, -1, -1):
            ans = right[i + 1] * nums[i + 1]
            right[i] = ans

        for i in range(len(nums)):
            ans = left[i] * right[i]
            output.append(ans)

        return output