class Solution:
    def solve(self, board: List[List[str]]) -> None:
        ROWS, COLS = len(board), len(board[0])
        
        q = collections.deque()
        for c in range(COLS):
            if board[0][c] == "O":
                q.append((0, c))

            if board[ROWS - 1][c] == "O":
                q.append((ROWS - 1, c))

        for r in range(ROWS):
            if board[r][0] == "O":
                q.append((r, 0))

            if board[r][COLS - 1] == "O":
                q.append((r, COLS - 1))
        
        visited = set()
        directions = [[0, 1], [0, -1], [1, 0], [-1, 0]]
        while q:
            row, col = q.popleft()
            if (row, col) not in visited:
                visited.add((row, col))

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


