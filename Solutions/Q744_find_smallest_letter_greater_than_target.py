class Solution(object):
    def nextGreatestLetter(self, letters, target):
        """
        :type letters: List[str]
        :type target: str
        :rtype: str
        """
        def ascii(n):
            return ord(n)

        letters = map(ascii, letters)
        target = ord(target)
        for elem in letters:
            if elem > target:
                return chr(elem)
        return chr(min(letters))
        