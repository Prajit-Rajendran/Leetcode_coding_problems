class Solution(object):
    def addBinary(self, a, b):
        """
        :type a: str
        :type b: str
        :rtype: str
        """
        if len(a)>len(b):
                b = "0"*(len(a) - len(b))+b
        elif len(a)<len(b):
                a = "0"*(len(b) - len(a))+a
        carry = 0
        bin_str = ''
        for i in range(len(a)-1, -1, -1):
            val = int(a[i]) + int(b[i]) + carry
            if val == 0:
                carry = 0
                bin_str = '0' + bin_str
            elif val == 1:
                carry = 0
                bin_str = '1' + bin_str
            elif val==2:
                carry = 1
                bin_str = '0' + bin_str
            elif val==3:
                carry = 1
                bin_str = '1' + bin_str
        if carry == 1:
            bin_str = '1' + bin_str
        return bin_str
            
        