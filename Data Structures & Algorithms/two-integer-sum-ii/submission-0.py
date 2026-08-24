class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        lp = 0
        rp = len(numbers) - 1

        while lp < rp:
            guess = numbers[lp] + numbers[rp]

            if guess == target:
                return [lp + 1, rp + 1]

            if guess > target:
                rp -= 1
            else:
                lp += 1
            
            