class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        ROWS, COLS = len(board), len(board[0])
        LENGTH = len(word)
        visited = set()

        curr = []
        def dfs(r: int, c: int, l: int) -> bool:
            if l == LENGTH:
                return True

            if (r < 0 or r >= ROWS or c < 0 or c >= COLS or l >= LENGTH
                or (r, c) in visited or board[r][c] != word[l]):
                return False

            visited.add((r, c))

            found = (dfs(r + 1, c, l + 1) or
                     dfs(r - 1, c, l + 1) or
                     dfs(r, c + 1, l + 1) or
                     dfs(r, c - 1, l + 1))

            visited.remove((r, c))

            return found

        for r in range(ROWS):
            for c in range(COLS):
                if dfs(r, c, 0):
                    return True

        return False

                
