class Solution:
    def numRescueBoats(self, people: List[int], limit: int) -> int:
        n = len(people)
        count=0
        people.sort()
        l, r = 0, n-1
        while l<=r:
            remain = limit - people[r]
            r-=1
            count+=1
            if l<=r and remain>=people[l]:
                l+=1
        return count
