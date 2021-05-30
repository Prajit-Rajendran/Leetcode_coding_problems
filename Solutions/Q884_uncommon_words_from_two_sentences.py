class Solution(object):
    def uncommonFromSentences(self, A, B):
        """
        :type A: str
        :type B: str
        :rtype: List[str]
        """
        A = A.split(' ')
        B = B.split(' ')
        A_dict = {}
        B_dict = {}
        for word in A:
            word = str(word)
            if word not in A_dict.keys():
                A_dict[word] = 1
            else:
                A_dict[word] += 1
        
        for word in B:
            word = str(word)
            if word not in B_dict.keys():
                B_dict[word] = 1
            else:
                B_dict[word] += 1
                
        uncommon = []
        for key in A_dict.keys():
            try:
                x = B_dict[key]
            except:
                if A_dict[key] == 1:
                    uncommon.append(key)
        
        for key in B_dict.keys():
            try:
                x = A_dict[key]
            except:
                if B_dict[key] == 1:
                    uncommon.append(key)
                    
        return uncommon       