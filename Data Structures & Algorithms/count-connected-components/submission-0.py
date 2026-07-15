class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        graph = [[] for i in range(n)]
        for u, v in edges:
            graph[u].append(v)
            graph[v].append(u)
        visited = [False]*n
        def dfs(node):
            visited[node]=True
            for nei in graph[node]:
                if not visited[nei]:
                    dfs(nei)
        count = 0
        for node in range(n):
            if not visited[node]:
                count+=1
                dfs(node)
        return count