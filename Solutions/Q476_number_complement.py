class Solution(object):
    def findComplement(self, num):
        """
        :type num: int
        :rtype: int
        """
        num = bin(num)[2:]
        comp = ''
        for c in num:
            if c=='0':
                comp += '1'
            else:
                comp += '0'
        return int(comp, 2)
        