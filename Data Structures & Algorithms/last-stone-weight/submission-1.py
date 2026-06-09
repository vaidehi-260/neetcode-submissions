class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        while len(stones)>1:
            stones = sorted(stones)
            n = len(stones)
            x = stones[n-1]
            y = stones[n-2]
            if x == y:
                stones.pop()
                stones.pop()
            elif x<y:
                stones.pop()
                stones.pop()
                stones.append(y-x)
            else:
                stones.pop()
                stones.pop()
                stones.append(x-y)
            if len(stones)<=1:
                break
        return stones[0] if stones else 0
