class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        for row in board:
            r = set()

            for num in row:
                if num == ".": continue
                if num in r: return False
                
                r.add(num)

        for i in range(9):
            c = set()
            for j in range(9):
                num = board[j][i]

                if num == ".": continue
                if num in c: return False

                c.add(num)

        boxes = []
        for i in range(0, 9, 3):
            for j in range(0, 9, 3):
                rows = board[i: i + 3]
                box = []
                for row in rows:
                    box.extend(row[j: j + 3])
                
                boxes.append(box)

        for box in boxes:
            b = set()

            for num in box:
                if num == ".": continue
                if num in b: return False
                
                b.add(num)

        return True
        
