class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        l = maxx = 0
        c = defaultdict(int)

        for r in range(len(s)):
            c[s[r]] += 1

            hi_f = max(c.values())
            repl = (r - l + 1) - hi_f
            if repl > k:
                c[s[l]] -= 1
                l += 1
            else:
                maxx = max(r - l + 1, maxx)

        return maxx