class Solution(object):
    def bitwiseComplement(self, N):
        """
        :type N: int
        :rtype: int
        """
        num = bin(N)[2:]
        comp = ''
        for c in num:
            if c=='0':
                comp += '1'
            else:
                comp += '0'
        return int(comp, 2)
        