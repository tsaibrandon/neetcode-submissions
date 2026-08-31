class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        def has_duplicates(cells):
            seen = set()
            for value in cells:
                if value == '.':
                    continue
                if value in seen:
                    return True
                seen.add(value)
            return False

        # Rows
        for i in range(9):
            row = [board[i][j] for j in range(9)]
            if has_duplicates(row):
                return False

        # Columns
        for j in range(9):
            col = [board[i][j] for i in range(9)]
            if has_duplicates(col):
                return False

        # 3x3 boxes
        for b in range(9):
            box_row = (b // 3) * 3
            box_col = (b % 3) * 3
            box = [
                board[r][c]
                for r in range(box_row, box_row + 3)
                for c in range(box_col, box_col + 3)
            ]
            if has_duplicates(box):
                return False

        return True