class Solution(object):
    def reverseOnlyLetters(self, S):
        """
        :type S: str
        :rtype: str
        """
        def return_ascii(letter):
            return ord(letter)
        
        def return_char(number):
            return chr(number)
        
        orig_S = S
        S = map(return_ascii, S)
        letters = []
        for num in S:
            if (num>=65 and num<=90) or (num>=97 and num<=122):
                letters.append(num)
        
        letters = list(reversed(letters))
        for i in range(len(S)):
            if (S[i]>=65 and S[i]<=90) or (S[i]>=97 and S[i]<=122):
                S[i] = letters[0]
                try:
                    letters = letters[1:]
                except:
                    pass
        
        return ''.join(map(return_char, S))
            
        