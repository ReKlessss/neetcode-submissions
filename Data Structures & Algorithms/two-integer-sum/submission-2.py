class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        # input: list numbers, a number to be added to

        # creating a hashmap of previously visited numbers: number | index
        # enumerate through nums and see if target - curr_num = hashmap (dictionary)
        # if it is, then return [dictionary[difference], i]
        # if not, put it in the hashmap

        # output: list of 2 numbers, that when used to find 2 numbers in the nums list, equal the target
        
        difference_map = {}
        for i, val in enumerate(nums):
            diff = target - val
            if diff in difference_map:
                return [difference_map[diff], i]
            
            difference_map[val] = i

        return

