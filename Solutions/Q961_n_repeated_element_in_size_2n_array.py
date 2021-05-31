class Solution(object):
    def repeatedNTimes(self, A):
        """
        :type A: List[int]
        :rtype: int
        """
        seen_dict = {}
        for elem in A:
            if elem not in seen_dict.keys():
                seen_dict[elem] = 1
            else:
                return elem