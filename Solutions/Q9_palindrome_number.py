class Solution(object):
    def isPalindrome(self, x):
        """
        :type x: int
        :rtype: bool
        """
        if x<0:
            return False
        if x>=0 and x<10:
            return True
        if x%11 == 0 and x<100:
            return True
        num_str = str(x)
        for i in range(len(num_str)):
            if num_str[i] != num_str[-1 - i]:
                return False
        return True
            
        