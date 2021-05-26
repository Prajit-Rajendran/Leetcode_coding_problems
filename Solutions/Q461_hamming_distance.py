class Solution(object):
    def hammingDistance(self, x, y):
        """
        :type x: int
        :type y: int
        :rtype: int
        """
        x = bin(x)[2:]
        y = bin(y)[2:]
        len_diff = abs(len(x) - len(y))
        max_len = len(x)
        if len(x) > len(y):
            y = '0'*len_diff + y
        elif len(x) < len(y):
            x = '0'*len_diff + x
            max_len = len(y)
        print(x, y)
        h_dist = 0
        for i in range(max_len):
            if x[i] != y[i]:
                h_dist += 1
        return h_dist
                
        