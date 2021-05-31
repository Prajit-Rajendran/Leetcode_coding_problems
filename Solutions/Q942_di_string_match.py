class Solution(object):
    def diStringMatch(self, S):
        """
        :type S: str
        :rtype: List[int]
        """
        res = [0]*(len(S)+1)
        possible_elem = [i for i in range(len(S)+1)]
        print(possible_elem)
        min_possible = 0
        max_possible = len(S)
        for i in range(len(S)):
            if S[i] == 'I':
                res[i] = min_possible
                possible_elem.remove(min_possible)
                min_possible += 1
            elif S[i] == 'D':
                res[i] = max_possible
                possible_elem.remove(max_possible)
                max_possible -= 1
        res[-1] = possible_elem[0]
        return res