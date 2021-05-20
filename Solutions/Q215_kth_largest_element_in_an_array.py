class Solution(object):
    def findKthLargest(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        while k>1:
            nums.remove(max(nums))
            k -= 1
        return max(nums)
        