class Solution(object):
    def missingNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        max_nums = max(nums)
        nums = list(sorted(nums))
        list_nums = [i for i in range(max_nums+1)]
        print(list_nums, nums)
        for i in range(min(len(nums), len(nums))):
            if nums[i] != list_nums[i]:
                return list_nums[i]
        return max_nums + 1