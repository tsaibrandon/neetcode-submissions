class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        """
        build an adj list
        add nodes and connections to the list

        create result var
        create visited set

        run dfs starting at 0
            each dfs run should check visited nodes
            once the connections complete add 1 to result

        return result
        """

        adj = [[] for _ in range(n)]

        for a, b in edges:
            adj[a].append(b)
            adj[b].append(a)

        visited = set()
        result = 0

        def dfs(node):
            visited.add(node)

            for neighbor in adj[node]:
                if neighbor not in visited:
                    dfs(neighbor)
  
        
        for node in range(n):
            if node not in visited:
                result += 1
                dfs(node)
            

        return result
        