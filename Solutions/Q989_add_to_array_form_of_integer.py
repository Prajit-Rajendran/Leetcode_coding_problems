class Solution(object):
    def addToArrayForm(self, A, K):
        """
        :type A: List[int]
        :type K: int
        :rtype: List[int]
        """
        A_str = ''
        for num in A:
            A_str += str(num)
        A_str = str(int(A_str) + K)
        res = []
        for c in A_str:
            res.append(int(c))
        return res
        
        