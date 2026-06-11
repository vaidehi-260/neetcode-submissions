class Solution:
    def partition(self, s: str) -> List[List[str]]:
        ans = []
        path = []
        def isPall(st):
            return st == st[::-1]
        def backtrack(start):
            if start == len(s):
                ans.append(path[:])
                return
            for i in range(start, len(s)):
                substring = s[start:i+1]
                if isPall(substring):
                    path.append(substring)
                    backtrack(i+1)
                    path.pop()
        backtrack(0)
        return ans