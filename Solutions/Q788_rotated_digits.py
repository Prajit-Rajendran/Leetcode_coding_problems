class Solution(object):
    def rotatedDigits(self, N):
        """
        :type N: int
        :rtype: int
        """
        good_nums = []
        for num in range(1, N+1):
            str_num = str(num)
            flag = 0
            flag2 = 0
            for c in str_num:
                if c in ['3', '4', '7']:
                    flag2 = 1
                    break
                if c in ['2', '5', '6', '9']:
                    flag = 1
            if flag == 1 and flag2 == 0:
                good_nums.append(num)
        return len(good_nums)
                
                    
        