class Solution(object):
    def detectCapitalUse(self, word):
        """
        :type word: str
        :rtype: bool
        """
        if word.lower() == word or word.upper() == word:
            return True
        elif word[0].upper() == word[0]:
            if word[1:].lower() == word[1:]:
                return True
        return False
        