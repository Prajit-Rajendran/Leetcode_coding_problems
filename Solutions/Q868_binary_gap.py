class Solution(object):
    def binaryGap(self, n):
        """
        :type n: int
        :rtype: int
        """
        bin_str = str(bin(n))
        bin_str = bin_str[2:]
        idx = []
        for i in range(len(bin_str)):
            if bin_str[i] == '1':
                idx.append(i)
        max_diff = 0
        for i in range(1, len(idx)):
            diff = idx[i] - idx[i-1]
            if diff > max_diff:
                max_diff = diff
        return max_diff
        