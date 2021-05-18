class Solution(object):
    def strStr(self, haystack, needle):
        """
        :type haystack: str
        :type needle: str
        :rtype: int
        """
        if needle == "":
            return 0
        if needle == haystack:
            return 0
        seq = len(needle)
        for i in range(len(haystack) - seq + 1):
            print(haystack[i:i+seq])
            if haystack[i:i+seq] == needle:
                return i
        return -1
        