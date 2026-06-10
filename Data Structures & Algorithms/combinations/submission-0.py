class Solution:
    def combine(self, n: int, k: int) -> List[List[int]]:
        ans = []
        def backtrack(i, comb):
            if i>n:
                if len(comb)==k:
                    ans.append(comb[:])
                return
            comb.append(i)
            backtrack(i+1, comb)
            comb.pop()
            backtrack(i+1, comb)
        backtrack(1, [])
        return ans
            