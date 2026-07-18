class DSU:
    def __init__(self, n):
        self.parent = list(range(n))
        self.rank = [0]*n
    def find(self, x):
        if self.parent[x]!=x:
            self.parent[x] = self.find(self.parent[x])
        return self.parent[x]
    def union(self, x, y):
        px = self.find(x)
        py = self.find(y)
        if px==py:
            return 
        if self.rank[px]<self.rank[py]:
            px, py = py, px
        self.parent[py]=px
        if self.rank[px]==self.rank[py]:
            self.rank[px]+=1
class Solution:
    def accountsMerge(self, accounts: List[List[str]]) -> List[List[str]]:
        n = len(accounts)
        dsu = DSU(n)
        email_to_accounts = {}
        for i, account in enumerate(accounts):
            for email in account[1:]:
                if email in email_to_accounts:
                    dsu.union(i, email_to_accounts[email])
                else:
                    email_to_accounts[email] = i
        groups = defaultdict(list)
        for email, idx in email_to_accounts.items():
            parent = dsu.find(idx)
            groups[parent].append(email)
        ans = []
        for parents, email in groups.items():
            ans.append([accounts[parents][0]] + sorted(email))
        return ans
