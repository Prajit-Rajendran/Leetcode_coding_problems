class Solution(object):
    def isIsomorphic(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        if len(set(s)) != len(set(t)):
            return False
        
        order_dict = {}
        for i in range(len(s)):
            if s[i] not in order_dict.keys():
                order_dict[s[i]] = t[i]
            else:
                if t[i] != order_dict[s[i]]:
                    return False
        return True
        