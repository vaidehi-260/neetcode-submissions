class Solution:
    def makesquare(self, matchsticks: List[int]) -> bool:
        total = sum(matchsticks)
        if total%4:
            return False
        target = total//4
        matchsticks.sort(reverse=True)
        sides = [0]*4
        def dfs(index):
            if index == len(matchsticks):
                return True
            stick = matchsticks[index]
            for i in range(4):
                if stick+sides[i]>target:
                    continue
                sides[i]+=stick
                if dfs(index+1):
                    return True 
                sides[i]-=stick
            return False
        return dfs(0)
        
