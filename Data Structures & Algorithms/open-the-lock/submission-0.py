from collections import deque
class Solution:
    def openLock(self, deadends: List[str], target: str) -> int:
        dead = set(deadends)
        if "0000" in dead:
            return -1
        q = deque(["0000"])
        visited={"0000"}
        turns=0
        while q:
            for i in range(len(q)):
                state = q.popleft()
                if state==target:
                    return turns
                for i in range(4):
                    digit = int(state[i])
                    for move in (-1,1):
                        newDigit = (digit+move)%10
                        newState = (state[:i]+ str(newDigit)+ state[i+1:])
                        if (newState not in dead and newState not in visited):
                            visited.add(newState)
                            q.append(newState)
            turns+=1
        return -1
