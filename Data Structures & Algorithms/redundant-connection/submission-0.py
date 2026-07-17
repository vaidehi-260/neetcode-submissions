class DSU:
    def __init__(self,n):
        self.parent=list(range(n+1))
        self.size = [1]*(n+1)
    def find(self, x):
        if self.parent[x]!=x:
            self.parent[x]= self.find(self.parent[x])
        return self.parent[x]
    def unite(self, a, b):
        rootA = self.find(a)
        rootB = self.find(b)
        if rootA == rootB:
            return 
        if self.size[rootA]<self.size[rootB]:
            rootA, rootB = rootB, rootA
        self.parent[rootB]=rootA
        self.size[rootA]+=self.size[rootB]
        return True
class Solution:
    def findRedundantConnection(self, edges: List[List[int]]) -> List[int]:
        n = len(edges)
        dsu = DSU(n)
        for u, v in edges:
            if not dsu.unite(u,v):
                return [u,v]
        