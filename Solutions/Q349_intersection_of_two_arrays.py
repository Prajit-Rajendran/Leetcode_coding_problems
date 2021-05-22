class Solution(object):
    def intersection(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: List[int]
        """
        intersect = []
        for n in nums1:
            try:
                nums2.remove(n)
                intersect.append(n)
            except:
                pass
            
        return set(intersect)
        