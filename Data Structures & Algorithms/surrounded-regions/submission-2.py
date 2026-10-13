class Solution:
    def solve(self, board: List[List[str]]) -> None:
        ROWS, COLS = len(board), len(board[0])
        q = collections.deque()
        visited = set()

        def add_border(r: int, c: int) -> None:
            if board[r][c] == "O" and (r, c) not in visited:
                q.append((r, c))
                visited.add((r, c))

        for c in range(COLS):
            add_border(0, c)
            add_border(ROWS - 1, c)

        for r in range(ROWS):
            add_border(r, 0)
            add_border(r, COLS - 1)
        
        directions = [[0, 1], [0, -1], [1, 0], [-1, 0]]
        while q:
            row, col = q.popleft()

            for nr, nc in directions:
                r = row + nr
                c = col + nc

                if 0 <= r < ROWS and 0 <= c < COLS and board[r][c] == "O" and (r, c) not in visited:
                    q.append((r, c))
                    visited.add((r, c))
        
        for r in range(ROWS):
            for c in range(COLS):
                if board[r][c] == "O" and (r, c) not in visited:
                    board[r][c] = "X"


