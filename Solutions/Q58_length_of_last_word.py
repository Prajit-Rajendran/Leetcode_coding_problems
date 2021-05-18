class Solution(object):
    def lengthOfLastWord(self, s):
        """
        :type s: str
        :rtype: int
        """
        if s==" ":
            return 0
        s = s.split(' ')
        if len(s) == 1:
            return len(s[0])
        for i in range(1,len(s)+1):
            if s[-i] != '':
                return len(s[-i])
        return 0
            
        
        