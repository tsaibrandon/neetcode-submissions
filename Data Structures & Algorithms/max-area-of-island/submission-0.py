class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
            """
            ROW, COL = length of rows, length of columns
            area = 0
            visited = set()

            handle empty input:
                return 0

            def bfs(row, col):
                q = deque()
                curr = 0

                mark the current space as visited
                add 1 to curr
                add curent space to q

                set directions

                while q is not empty:
                    r, c = pop the left 

                    for dr, dc in directions:
                        nr, nc = r + dr, c + dc

                        if the new space is inbounds, land, and not visited:
                            mark new space as visited
                            add 1 to curr
                            add it to the q 
                
                return curr

            go through each space in the grid:
                if the space is land and has not been visited:
                    area = max(area, bfs(current space))
            
            return area
            """

            ROWS, COLS = len(grid), len(grid[0])
            area = 0
            visited = set()

            if not grid:
                return 0

            def bfs(row, col):
                q = deque()
                curr = 0

                visited.add((row, col))
                curr += 1
                q.append((row, col))

                directions = [(1, 0), (-1, 0), (0, 1), (0, -1)]

                while q:
                    r, c = q.popleft()
                    
                    for dr, dc in directions:
                        nr, nc = r + dr, c + dc

                        if 0 <= nr < ROWS and 0 <= nc < COLS and grid[nr][nc] == 1 and (nr, nc) not in visited:
                            visited.add((nr, nc))
                            curr += 1
                            q.append((nr, nc))
                
                return curr

            for r in range(ROWS):
                for c in range(COLS):
                    if grid[r][c] == 1 and (r, c) not in visited:
                        area = max(area, bfs(r, c))
            
            return area