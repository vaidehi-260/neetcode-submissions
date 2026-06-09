class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        result = []
        for i in range(len(temperatures)):
            found = False
            for j in range(i+1, len(temperatures)):
                if temperatures[j]>temperatures[i]:
                    result.append(j-i)
                    found = True
                    break
            if not found:
                result.append(0)
        return result

            
