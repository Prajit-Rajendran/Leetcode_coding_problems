class Solution(object):
    def sortArrayByParity(self, A):
        """
        :type A: List[int]
        :rtype: List[int]
        """
        odd = []
        even = []
        for num in A:
            if num%2 == 0:
                even.append(num)
            else:
                odd.append(num)
        return even+odd
        