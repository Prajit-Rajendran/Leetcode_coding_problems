class Solution(object):
    def uniqueMorseRepresentations(self, words):
        """
        :type words: List[str]
        :rtype: int
        """
        morse_dict = {'A':".-",'B':"-...",'C':"-.-.",'D':"-..",'E':".",'F':"..-.",'G':"--.",'H':"....",'I':"..",'J':".---",'K':"-.-",'L':".-..",'M':"--",'N':"-.",'O':"---",'P':".--.",'Q':"--.-",'R':".-.",'S':"...",'T':"-",'U':"..-",'V':"...-",'W':".--",'X':"-..-",'Y':"-.--", 'Z':"--.."}
    
        morse_codes = []
        for word in words:
            word = word.upper()
            cur_code = ""
            for c in word:
                cur_code += morse_dict[c]
            morse_codes.append(cur_code)
        return len(list(set(morse_codes)))
        