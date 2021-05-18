class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        for i in range(len(nums)):
            number = nums[i]
            if (target-number) in nums:
                return [i, nums.index(target-number)]