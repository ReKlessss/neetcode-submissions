class Solution:
    def partition(self, s: str) -> List[List[str]]:
        res, curr = [], []
        
        def dfs(start: int) -> None:
            if start >= len(s):
                res.append(curr.copy())
                return

            for end in range(start, len(s)):
                snippet = s[start : end + 1]
                if snippet == snippet[::-1]:
                    curr.append(snippet)
                    dfs(end + 1)
                    curr.pop()

        dfs(0)
        return res