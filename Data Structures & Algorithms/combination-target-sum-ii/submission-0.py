class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        candidates.sort()
        sets = []
        ans = []
        def backtracking(i, total):
            if total==target:
                ans.append(sets[:])
                return
            if total>target:
                return
            for j in range(i, len(candidates)):
                if j >i and candidates[j]==candidates[j-1]:
                    continue
                sets.append(candidates[j])
                backtracking(j+1, total+ candidates[j])
                sets.pop()

        backtracking(0,0)
        return ans