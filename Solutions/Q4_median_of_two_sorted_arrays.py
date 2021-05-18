class Solution(object):
    def findMedianSortedArrays(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: float
        """
        n = len(nums1)+len(nums2)
        flag = ''
        if n%2==0:
            flag = 'even'
        else:
            flag = 'odd'
        elems = []
        while len(elems)<(n/2)+1:
            if len(nums1) == 0:
                elems.append(nums2[0])
                nums2.remove(nums2[0])
            elif len(nums2) == 0:
                elems.append(nums1[0])
                nums1.remove(nums1[0])
            elif nums1[0]<=nums2[0]:
                elems.append(nums1[0])
                nums1.remove(nums1[0])
            else:
                elems.append(nums2[0])
                nums2.remove(nums2[0])
        if flag == 'even':
            return float((elems[-1] + elems[-2]))/2
        else:
            return elems[-1]
                
        