class Solution(object):
    def commonChars(self, A):
        """
        :type A: List[str]
        :rtype: List[str]
        """
        letters_dict = {}
        for c in A[0]:
            if c not in letters_dict.keys():
                letters_dict[c] = 1
            else:
                letters_dict[c] += 1

        
        for i in range(1, len(A)):
            for key in letters_dict.keys():
                if key not in A[i]:
                    letters_dict.pop(key)
                else:
                    letters_dict[key] = min(letters_dict[key], A[i].count(key))
                    
        res = []
        for key in letters_dict.keys():
                res += [key]*letters_dict[key]
        return res
                    
                    
        