class Solution(object):
    import math
    def search(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        low = 0
        high = len(nums)-1
        while low<=high:
            med = (low+high)/2
            if target>nums[med]:
                low = med+1
            elif target<nums[med]:
                high = med-1
            else:
                return med
        return -1
                
        