class Solution(object):
    def removeOuterParentheses(self, S):
        """
        :type S: str
        :rtype: str
        """
        val = 0
        edge_indices = [0]
        for i in range(len(S)):
            if S[i] == '(':
                val += 1
            elif S[i] == ')':
                val -= 1
            if val == 0:
                edge_indices.append(i)
        
        res = ''
        for i in range(len(S)-1):
            if i==1 and S[1] != ')':
                res += S[i]
            elif i!=1 and i not in edge_indices:
                if i-1 not in edge_indices:
                    res += S[i]
        return res
                
        