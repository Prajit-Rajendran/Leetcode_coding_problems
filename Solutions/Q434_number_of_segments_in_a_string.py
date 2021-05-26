class Solution(object):
    def countSegments(self, s):
        """
        :type s: str
        :rtype: int
        """
        if s=="":
            return 0
        s = s.split(' ')
        s = [str(c) for c in s]
        new_s = []
        for c in s:
            if c != '':
                new_s.append(c)
        print(new_s)
        return len(new_s)
        