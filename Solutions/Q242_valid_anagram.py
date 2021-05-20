class Solution(object):
    def isAnagram(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        if len(s) != len(t):
            return False
        for elem in s:
            try:
                s_count = s.count(elem)
                t_count = t.count(elem)
                if s_count != t_count:
                    return False
            except:
                return False
        return True
        