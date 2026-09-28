class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        """
        ROWS, COLS = len of rows, len of cols
        time = 0
        fresh = 0
        q = deque()

        go through the entire grid:
            if the space == 2:
                add it to the q
            if the space == 1:
                add 1 to fresh

        directions = [(1, 0), (-1, 0), (0, -1), (0, 1)]
        
        while q is not empty:;
            for len of the q:
                r, c = popleft()

                for each direction:
                    nr, nc = new row, new col

                    if nr and nc are inbound and the space == 1:
                        add the new space into the q
                        update new space to 2
                        subtract 1 from fresh

            add 1 to time
        
        if fresh == 0:
            return time
        else;
            return -1
        """
        ROWS, COLS = len(grid), len(grid[0])
        time = 0
        fresh = 0
        q = deque()

        for r in range(ROWS):
            for c in range(COLS):
                if grid[r][c] == 2:
                    q.append((r, c))
                if grid[r][c] == 1:
                    fresh += 1
        
        directions = [(1, 0), (-1, 0), (0, -1), (0, 1)]

        while q and fresh > 0:
            for _ in range(len(q)):
                r, c = q.popleft()

                for dr, dc in directions:
                    nr, nc = r + dr, c + dc

                    if 0 <= nr < ROWS and 0 <= nc < COLS and grid[nr][nc] == 1:
                        q.append((nr, nc))
                        grid[nr][nc] = 2
                        fresh -= 1
            
            time += 1

        if fresh == 0:
            return time
        else:
            return -1