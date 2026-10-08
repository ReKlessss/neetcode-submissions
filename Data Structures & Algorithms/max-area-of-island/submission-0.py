class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        if not grid: return 0

        rows, cols = len(grid), len(grid[0])
        visited = set()
        maxx = 0

        # perform bfs, increasing the size whenever moving on
        def bfs(r: int, c: int) -> int:
            q = collections.deque()
            visited.add((r, c))
            q.append((r, c))
            area = 1

            while q:
                row, col = q.popleft()
                directions = [(0, 1), (0, -1), (1, 0), (-1, 0)]

                for nr, nc in directions:
                    r = row + nr
                    c = col + nc

                    if (0 <= r < rows and 0 <= c < cols and
                        (r, c) not in visited and grid[r][c] == 1):
                        q.append((r, c))
                        visited.add((r, c))
                        area += 1

            return area

        # loop through every space, skipping if its not an island
        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == 1 and (r, c) not in visited:
                    area = bfs(r, c)
                    maxx = max(maxx, area)
                    
        return maxx
