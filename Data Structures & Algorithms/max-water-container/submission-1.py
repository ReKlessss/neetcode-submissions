class Solution:
    def maxArea(self, heights: List[int]) -> int:
        l = maxx = 0
        r = len(heights) - 1

        while l < r:
            hl, hr = heights[l], heights[r]
            vol = (r - l) * min(hl, hr)
            maxx = max(maxx, vol)

            if hl <= hr:
                l += 1
            else:
                r -= 1

        return maxx


        
        
        

        return maxx