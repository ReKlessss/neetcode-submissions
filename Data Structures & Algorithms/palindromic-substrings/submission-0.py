class Solution:
    def countSubstrings(self, s: str) -> int:
        def expand(l: int, r: int) -> int:
            if l >= 0 and r < len(s) and s[l] == s[r]:
                return expand(l - 1, r + 1) + 1
            
            return 0
        
        res = 0
        for i in range(len(s)):
            res += expand(i, i)
            res += expand(i, i + 1)

        return res