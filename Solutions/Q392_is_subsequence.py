class Solution(object):
    def isSubsequence(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        for i in range(len(t)):
            try:
                if t[i] == s[0]:
                    s = s[1:]
            except:
                pass
        if len(s) > 0:
            return False
        return True
            
        