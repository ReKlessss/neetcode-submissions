class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        sn = sorted(nums)
        zeros = []
        
        for i, l in enumerate(sn):
            if i > 0 and sn[i] == sn[i-1]: continue
            m, r = i + 1, len(sn) - 1
            
            while m < r:
                g = l + sn[m] + sn[r]
                if g > 0:
                    r -= 1
                elif g < 0:
                    m += 1
                else:
                    zeros.append([l, sn[m], sn[r]])
                    m += 1
                    while m < r and sn[m] == sn[m - 1]:
                        m += 1
        
        return zeros
        