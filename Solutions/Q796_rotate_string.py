class Solution(object):
    def rotateString(self, A, B):
        """
        :type A: str
        :type B: str
        :rtype: bool
        """
        if A == "" and B == "":
            return True
        if len(A) == 1 and len(B) == 1 and A[0] == B[0]:
            return True
        str_combi = B
        for i in range(len(B)):
            str_combi = str_combi[1:] + B[i]
            if str_combi == A:
                return True
        return False
        