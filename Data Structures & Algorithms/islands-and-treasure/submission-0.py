class Solution:
    def islandsAndTreasure(self, grid: List[List[int]]) -> None:
        """
        ROWS, COLS = num of rows, num of cols
        q = deque()
        
        go through the grid:
            if the space is 0:
                add it to the q
        
        while q is not empty:
            r, c = pop left q

            for each direction:
                nr, nc = new row, new column

                if the new space is in bounds and land:
                    add new space to the q
                    set that space to the old space + 1
        """
        ROWS, COLS = len(grid), len(grid[0])
        LAND = 2 ** 31 - 1
        q = deque()

        for r in range(ROWS):
            for c in range(COLS):
                if grid[r][c] == 0:
                    q.append((r, c))
        
        directions = [(1,0), (-1, 0), (0, 1), (0, -1)]

        while q:
            r, c = q.popleft()

            for dr, dc in directions:
                nr, nc = r + dr, c + dc

                if 0 <= nr < ROWS and 0 <= nc < COLS and grid[nr][nc] == LAND:
                    q.append((nr, nc))
                    grid[nr][nc] = grid[r][c] + 1
