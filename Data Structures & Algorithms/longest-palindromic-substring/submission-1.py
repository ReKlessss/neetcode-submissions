class Solution:
    def longestPalindrome(self, s: str) -> str:
        if not s:
            return ""

        start, maxx = 0, 0

        def expand(l: int, r: int) -> int:
            while l >= 0 and r < len(s) and s[l] == s[r]:
                l -= 1
                r += 1

            return r - l - 1

        for i in range(len(s)):
            len1 = expand(i, i)
            len2 = expand(i, i + 1)

            curr = max(len1, len2)
            if curr > maxx:
                maxx = curr
                start = i - ((curr - 1) // 2)

        return s[start : start + maxx]