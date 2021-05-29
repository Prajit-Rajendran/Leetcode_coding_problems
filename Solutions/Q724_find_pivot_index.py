class Solution(object):
    def pivotIndex(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        total_sum = sum(nums)
        for i in range(len(nums)):
            left_sum = sum(nums[:i])
            right_sum = total_sum - left_sum - nums[i]
            if left_sum == right_sum:
                return i
        return -1
            
        