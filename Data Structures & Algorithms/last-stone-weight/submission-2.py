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
            else:
                stones.pop()
                stones.pop()
                stones.append(x-y)
        return stones[0] if stones else 0
