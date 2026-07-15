class Solution:
    def validTree(self, n: int, edges: List[List[int]]) -> bool:
        if len(edges)!=n-1:
            return False
        graph = [[] for i in range(n)]
        for u,v in edges:
            graph[u].append(v)
            graph[v].append(u)
        visited = [False]*n
        def dfs(node, parent):
            visited[node]=True
            for nei in graph[node]:
                if not visited[nei]:
                    if not dfs(nei, node):
                        return False
                elif nei!=parent:
                    return False
            return True
        if not dfs(0, -1):
            return False
        return all(visited)