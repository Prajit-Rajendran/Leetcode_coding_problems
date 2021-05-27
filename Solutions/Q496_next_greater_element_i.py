class Solution(object):
    def nextGreaterElement(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: List[int]
        """
        soln = []
        for elem in nums1:
            try:
                idx = nums2.index(elem)
                flag = 0
                for i in range(idx, len(nums2)):
                    if nums2[i] > elem and flag == 0:
                        flag = 1
                        soln.append(nums2[i])
                        continue
                if flag == 0:
                    soln.append(-1)
            except:
                soln.append(-1)
        return soln
                