class Solution(object):
    def dominantIndex(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if len(nums) == 1:
            return 0
        max_num = max(nums)
        idx = nums.index(max_num)
        nums.remove(max_num)
        if max_num >= 2*max(nums):
            return idx
        return -1
        