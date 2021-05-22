class Solution(object):
    def isPowerOfFour(self, n):
        """
        :type n: int
        :rtype: bool
        """
        if n == 1:
            return True
        while n>1:
            n = n/4.0
            if n == 1:
                return True
        return False
        