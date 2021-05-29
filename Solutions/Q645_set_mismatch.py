class Solution(object):
    def findErrorNums(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        num_dict = {}
        repeated_num = -1
        for elem in nums:
            if elem not in num_dict.keys():
                num_dict[elem] = 1
            else:
                repeated_num = elem
        numbers = [i for i in range(1, len(nums)+1)]
        #print(repeated_num, numbers)
        for key in num_dict.keys():
            try:
                if len(numbers)>1:
                    numbers.remove(key)
            except:
                pass
        return [repeated_num, numbers[0]]
        