class Solution(object):
    def findJudge(self, N, trust):
        """
        :type N: int
        :type trust: List[List[int]]
        :rtype: int
        """
        if N == 1:
            return  1
        trust_dict = {}
        trusted_dict = {}
        for elem in trust:
            if elem[1] not in trust_dict.keys():
                trust_dict[elem[1]] = [elem[0]]
            else:
                trust_dict[elem[1]].append(elem[0])
            if elem[0] not in trusted_dict.keys():
                trusted_dict[elem[0]] = [elem[1]]
            else:
                trusted_dict[elem[0]].append(elem[1]) 
        for key in trust_dict.keys():
            if len(trust_dict[key]) == N-1:
                try:
                    x = trusted_dict[key]
                except:
                    return key
        return -1
            
            