class Solution(object):
    def checkRecord(self, s):
        """
        :type s: str
        :rtype: bool
        """
        if len(s)<2:
            return True
        prev = s[0]
        prev2 = s[1]
        absent = 0
        if s[0:2] == 'AA':
            return False
        if prev == 'A' or prev2 == 'A':
            absent += 1
        for i in range(2, len(s)):
            cur = s[i]
            print(prev, prev2,  cur, absent)
            if cur == 'A':
                absent += 1
            if absent > 1:
                return False
            if cur == 'L' and prev == 'L' and prev2 == 'L':
                return False
            prev = prev2
            prev2 = cur
        return True
        