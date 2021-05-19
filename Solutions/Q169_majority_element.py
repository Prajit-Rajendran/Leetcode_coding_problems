class Solution(object):
    def majorityElement(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        maj = int(len(nums)/2) + 1
        print(maj)
        unique_nums = list(set(nums))
        count = 0
        for i in range(len(unique_nums)):
            if nums.count(unique_nums[i]) >= maj:
                return unique_nums[i]
        