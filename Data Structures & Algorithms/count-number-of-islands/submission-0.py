class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        """
        islands = 0
        visited = set()

        go through entire grid, space by space
            if space is land and not visited
                add 1 to islands
                run bfs on current spot
            else:
                move onto the next space

        bfs will check the spaces around
            q = deque

            add space to visited
            add space to q

            while q is not empty
                check the spaces up left down right
                    if the space is inbound, land, and not visited
                        add it to visited
                        add it to the q
        
        return islands
        """

        ROWS, COLS = len(grid), len(grid[0])
        islands = 0
        visited = set()

        def bfs(row, col):
            q = deque()

            visited.add((row, col))
            q.append((row, col))

            directions = [(0, 1), (0, -1), (1, 0), (-1, 0)]

            while q:
                r, c = q.popleft()

                for dr, dc in directions:
                    nr = r + dr
                    nc = c + dc

                    if 0 <= nr < ROWS and 0 <= nc < COLS and grid[nr][nc] == "1" and (nr, nc) not in visited:
                        visited.add((nr, nc))
                        q.append((nr, nc))

        for r in range(ROWS):
            for c in range(COLS):
                if grid[r][c] == "1" and (r, c) not in visited:
                    islands += 1
                    bfs(r, c)

        return islands




        