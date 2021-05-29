class Solution(object):
    def backspaceCompare(self, S, T):
        """
        :type S: str
        :type T: str
        :rtype: bool
        """
        stack_S = []
        for elem in S:
            if elem!='#':
                stack_S.append(str(elem))
            else:
                stack_S = stack_S[:-1]
        
        stack_T = []
        for elem in T:
            if elem!='#':
                stack_T.append(str(elem))
            else:
                stack_T = stack_T[:-1]
                
        return stack_S == stack_T