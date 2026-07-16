class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        graph = [[] for i in range(numCourses)]
        for courses, pre in prerequisites:
            graph[pre].append(courses)
        visited=[False]*numCourses
        path = [False]*numCourses
        order = []
        def dfs(node):
            visited[node]=True
            path[node]=True
            for nei in graph[node]:
                if not visited[nei]:
                    if not dfs(nei):
                        return False
                elif path[nei]:
                    return False
            path[node]=False
            order.append(node)
            return True
        for i in range(numCourses):
            if not visited[i]:
                if not dfs(i):
                    return []
        return order[::-1]
        