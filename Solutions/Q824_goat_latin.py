class Solution(object):
    def toGoatLatin(self, S):
        """
        :type S: str
        :rtype: str
        """
        final_word = ""
        S = S.split(' ')
        for i in range(len(S)):
            flag = 0
            word = S[i]
            if word[0] in ['A', 'a', 'E', 'e', 'I', 'i', 'O', 'o', 'U', 'u']:
                flag = 1
            if flag == 1:
                final_word = final_word + word + "ma" + "a"*(i+1)
            else:
                final_word = final_word + word[1:] + word[0] + "ma" + "a"*(i+1)
            if i != len(S) - 1:
                final_word = final_word + " "
            #print(final_word)
        return final_word
                
                
            
            
        