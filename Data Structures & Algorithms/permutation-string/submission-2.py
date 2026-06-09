class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        c1={}
        for c in s1:
            c1[c] = 1+c1.get(c, 0)
        need = len(c1)
        for i in range(len(s2)):
            c2, curr= {}, 0
            for j in range(i, len(s2)):
                c2[s2[j]] = 1+ c2.get(s2[j], 0)
                if c1.get(s2[j], 0) < c2[s2[j]]:
                    break
                if c1.get(s2[j], 0)==c2[s2[j]]:
                    curr+=1
                if curr == need:
                    return True 
        return False
                