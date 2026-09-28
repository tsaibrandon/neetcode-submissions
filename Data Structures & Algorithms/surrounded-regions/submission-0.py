class Solution:
    def solve(self, board: List[List[str]]) -> None:
        """
         - empty matrix -> 
         - connected up down left right
         - modified in place
         - yes only x and o

        if board is empty:
            return

        go through the entire board:
            add all border o cells into a q
            mark cell as b
        
        while the q is not empty:
            pop the left 
            check all directions
            if the neighbor is inbound, == o
                add it to the q
                mark it b
        
        go through the entire board:
            if the cell is o:
                change it to x
            if the cell is b:
                change it to o
        """
        # return if board is empty
        if not board:
            return

        ROWS, COLS = len(board), len(board[0])
        q = deque()

        # add boarder "O"s to a q
        for r in range(ROWS):
            for c in range(COLS):
                if (r == 0 or r == ROWS - 1 or c == 0 or c == COLS - 1) and board[r][c] == "O":
                    q.append((r, c))
                    board[r][c] = "B"

        directions = [(1, 0), (-1, 0), (0, -1), (0, 1)]
        
        # find adjacent "O"s to border "O"
        while q:
            r, c = q.popleft()

            for dr, dc in directions:
                nr, nc = r + dr, c + dc

                if 0 <= nr < ROWS and 0 <= nc < COLS and board[nr][nc] == "O":
                    q.append((nr, nc))
                    board[nr][nc] = "B"
        
        # change board in place
        for r in range(ROWS):
            for c in range(COLS):
                if board[r][c] == "O":
                    board[r][c] = "X"
                if board[r][c] == "B":
                    board[r][c] = "O"



