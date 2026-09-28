class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        rows, cols = len(heights), len(heights[0])
        result = []

        if not heights:
            return []

        def bfs(start):
            q = deque(start)
            visited = set(start)

            directions = [(1, 0), (-1, 0), (0, -1), (0, 1)]

            while q:
                r, c = q.popleft()

                for dr, dc in directions:
                    nr, nc = r + dr, c + dc

                    if 0 <= nr < rows and 0 <= nc < cols and (nr, nc) not in visited and heights[nr][nc] >= heights[r][c]:
                        visited.add((nr, nc))
                        q.append((nr, nc))

            return visited  

        pacific_start = []
        atlantic_start = []

        for r in range(rows):
            pacific_start.append((r, 0))
            atlantic_start.append((r, cols - 1))

        for c in range(cols):
            pacific_start.append((0, c))
            atlantic_start.append((rows - 1, c))

        pacific = bfs(pacific_start)
        atlantic = bfs(atlantic_start)

        for r in range(rows):
            for c in range(cols):
                if (r, c) in pacific and (r, c) in atlantic:
                    result.append([r, c])

        return result
