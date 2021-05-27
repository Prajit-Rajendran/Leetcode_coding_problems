class Solution(object):
    def findMaxConsecutiveOnes(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        max_cons = 0
        cur_cons = 0
        for val in nums:
            if val == 1:
                cur_cons += 1
            if cur_cons > max_cons:
                max_cons = cur_cons
            if val != 1:
                cur_cons = 0
        return max_cons
        