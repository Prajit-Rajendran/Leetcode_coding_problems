class Solution(object):
    def reverse(self, x):
        """
        :type x: int
        :rtype: int
        """
        if x>=0 and x<10:
            return x
        minus = 0
        if x<0:
            minus = 1
            x = x*-1
        num_str = str(x)
        num_copy = [num_str[i] for i in range(len(num_str)-1,-1,-1)]
        while num_copy[0] == '0':
            num_copy = num_copy[1:]
        num = ''.join(num_copy)
        if int(num)>=2147483648:
            return 0
        if minus == 1:
            num = '-'+num
        return num