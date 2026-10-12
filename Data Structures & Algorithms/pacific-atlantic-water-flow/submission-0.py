class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        rows, cols = len(heights), len(heights[0])
        paci, atla = set(), set()
        
        def dfs(r: int, c: int, visited, prev_height: int):
            if ((r, c) in visited or r < 0 or c < 0 or 
                r == rows or c == cols or heights[r][c] < prev_height):
                return

            visited.add((r, c))
            dfs(r + 1, c, visited, heights[r][c])
            dfs(r - 1, c, visited, heights[r][c])
            dfs(r, c + 1, visited, heights[r][c])
            dfs(r, c - 1, visited, heights[r][c])

        for c in range(cols):
            dfs(0, c, paci, heights[0][c])
            dfs(rows - 1, c, atla, heights[rows - 1][c])

        for r in range(rows):
            dfs(r, 0, paci, heights[r][0])
            dfs(r, cols - 1, atla, heights[r][cols - 1])

        res = []
        for r, c in paci:
            if (r, c) in atla:
                res.append([r, c])

        return res