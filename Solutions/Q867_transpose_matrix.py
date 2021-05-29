class Solution(object):
    def transpose(self, A):
        """
        :type A: List[List[int]]
        :rtype: List[List[int]]
        """
        rows = len(A)
        cols = len(A[0])
        B = []
        for i in range(cols):
            temp = [0]*rows
            B.append(temp)
        for i in range(rows):
            for j in range(cols):
                B[j][i] = A[i][j]
        return B
        