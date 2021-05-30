class Solution(object):
    def smallestRangeI(self, A, K):
        """
        :type A: List[int]
        :type K: int
        :rtype: int
        """
        max_A = max(A)
        B = []
        for elem in A:
            if elem == max_A:
                B.append(max_A - K)
                continue
            if elem + K > max_A - K:
                B.append(max_A - K)
            else:
                B.append(elem + K)
        print(B)
        return max(B)-min(B)
            
        