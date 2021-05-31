class Solution(object):
    def kClosest(self, points, K):
        """
        :type points: List[List[int]]
        :type K: int
        :rtype: List[List[int]]
        """
        def orig_dist(v1):
            return v1[0]**2 + v1[1]**2
        
        dist = []
        for i in range(len(points)):
            dist.append((i, orig_dist(points[i])))
            
        dist = sorted(dist, key=lambda x: x[1])        
        dist = dist[: K]
        
        closest = []
        for elem in dist:
            closest.append(points[elem[0]])
            
        return closest
        