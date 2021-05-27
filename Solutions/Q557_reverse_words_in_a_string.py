class Solution(object):
    def reverseWords(self, s):
        """
        :type s: str
        :rtype: str
        """
        news = ""
        s = s.split(' ')
        for c in s:
            c = str(c)[::-1]
            news += c
            news += " "
        return news[:-1]
        