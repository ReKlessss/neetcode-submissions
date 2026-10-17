class Solution:
    def partition(self, s: str) -> List[List[str]]:
        res, curr = [], []
        
        def dfs(start: int) -> None:
            if start >= len(s):
                res.append(curr.copy())
                return

            for end in range(start, len(s)):
                snippet = s[start : end + 1]
                if self.is_palindrome(snippet):
                    curr.append(snippet)
                    dfs(end + 1)
                    curr.pop()

        dfs(0)
        return res

    def is_palindrome(self, s: str) -> bool:
        l, r = 0, len(s) - 1

        while l < r:
            if s[l] != s[r]:
                return False

            l += 1
            r -= 1

        return True