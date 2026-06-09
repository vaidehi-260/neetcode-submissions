class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        dist={}
        for i in range(len(points)):
            dist[i]=((points[i][0]**2) + (points[i][1]**2))
        ans = []
        for j in range(k):
            min_i = min(dist, key = dist.get)
            ans.append(points[min_i])
            dist.pop(min_i)
        return ans