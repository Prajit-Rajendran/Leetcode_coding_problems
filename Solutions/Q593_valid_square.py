class Solution(object):
    def validSquare(self, p1, p2, p3, p4):
        """
        :type p1: List[int]
        :type p2: List[int]
        :type p3: List[int]
        :type p4: List[int]
        :rtype: bool
        """
        tuples = len(list(set([(p1[0],p1[1]), (p2[0],p2[1]), (p3[0],p3[1]), (p4[0],p4[1])])))
        if tuples<4:
            return False
        def dist(point1, point2)a:
            (a,b) = point1
            (c,d) = point2
            return (a-c)**2 + (b-d)**2
        
        distances = [dist(p1, p2), dist(p1, p3), dist(p1, p4), dist(p2, p3), dist(p2, p4), dist(p3,p4)]
        unique = list(set(distances))
        if len(unique)==2:
            if distances.count(unique[0]) in [2,4]:
                return True
        return False
        