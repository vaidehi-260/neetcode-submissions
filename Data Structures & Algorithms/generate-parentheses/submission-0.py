class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        ans = []
        perm = []
        def backtrack(openN, closeN):
            if openN == closeN == n:
                ans.append("".join(perm))
                return
            if openN<n:
                perm.append("(")
                backtrack(openN+1, closeN)
                perm.pop()
            if closeN<n and openN>closeN:
                perm.append(")")
                backtrack(openN, closeN+1)
                perm.pop()
        backtrack(0,0)
        return ans
                