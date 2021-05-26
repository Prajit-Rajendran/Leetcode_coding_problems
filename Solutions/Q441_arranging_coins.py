class Solution(object):
    def arrangeCoins(self, n):
        """
        :type n: int
        :rtype: int
        """
        if n == 1:
            return 1
        k = 1
        while n >= k:
            n = n - k
            k = k + 1
        return k - 1
        