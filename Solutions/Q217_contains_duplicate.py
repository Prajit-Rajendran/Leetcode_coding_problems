class Solution(object):
    def containsDuplicate(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        nums_dict = {}
        for n in nums:
            try:
                nums_dict[n] += 1
                return True
            except:
                nums_dict[n] = 1
        return False
        