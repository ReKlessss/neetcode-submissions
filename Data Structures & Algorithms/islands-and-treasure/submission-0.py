class Solution:
    def islandsAndTreasure(self, grid: List[List[int]]) -> None:
        rows, cols = len(grid), len(grid[0])
        q = collections.deque()
        inf = (2 ** 31) - 1

        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == 0:
                    q.append((r, c))     

        directions = [(0, 1), (0, -1), (1, 0), (-1, 0)]
        while q:
            row, col = q.popleft()

            for nr, nc in directions:
                r = row + nr
                c = col + nc

                if 0 <= r < rows and 0 <= c < cols and grid[r][c] == inf:
                    grid[r][c] = grid[row][col] + 1
                    q.append((r, c))