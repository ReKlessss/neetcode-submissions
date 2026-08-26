class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        c = set()

        for n in nums:
            if n in c:
                return True
            
            c.add(n)
        
        return False