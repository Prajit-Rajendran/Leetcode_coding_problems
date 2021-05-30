class Solution(object):
    def minDeletionSize(self, A):
        """
        :type A: List[str]
        :rtype: int
        """        
        rows = len(A)
        cols = len(A[0])
        print(cols)
        if cols == 1:
            if ord(str(A[0])) > ord(str(A[1])):
                return 1
            else:
                return 0
        matrix = []
        for i in range(cols):
            matrix.append([0]*rows)
        for i in range(rows):
            for j in range(cols):
                matrix[j][i] = ord(str(A[i][j]))
        print(matrix)
        count = 0
        for i in range(cols):
            if matrix[i] != sorted(matrix[i]):
                count += 1
        return count
                