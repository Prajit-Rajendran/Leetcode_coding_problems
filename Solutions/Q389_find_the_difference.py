class Solution(object):
    def findTheDifference(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: str
        """
        if s == "":
            return t
        t = list(t)
        for c in s:
            t.remove(c)
        return "".join(t)
        