class Solution(object):
    def isPalindrome(self, s):
        """
        :type s: str
        :rtype: bool
        """
        if s == "":
            return True
        front = ''
        back = ''
        for c in s:
            ascii = ord(c)
            if ascii >=65 and  ascii <= 90 or ascii >=97 and  ascii <= 122:
                c = c.lower()
                front = front + c
                back = c + back
            elif c in ['1','2','3','4','5','6','7','8','9','0']:
                front = front + c
                back = c + back
        print(front, back)
        return front == back
        