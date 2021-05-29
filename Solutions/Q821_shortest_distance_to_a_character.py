class Solution(object):
    def shortestToChar(self, S, C):
        """
        :type S: str
        :type C: str
        :rtype: List[int]
        """
        c_indices = []
        for i in range(len(S)):
            if S[i] == C:
                c_indices.append(i)
        
        def min_dist(elem, A):
            B = []
            for i in range(len(A)):
                B.append(abs(A[i] - elem))
            return min(B)
                
        res = [0]*len(S)
        for i in range(len(S)):
            if S[i] == C:
                continue
            res[i] = min_dist(i, c_indices)
        return res
            
            
            
        