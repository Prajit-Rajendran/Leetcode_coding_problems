class Solution(object):
    def selfDividingNumbers(self, left, right):
        """
        :type left: int
        :type right: int
        :rtype: List[int]
        """
        res = []
        for i in range(left, right+1):
            num = str(i)
            if '0' in num:
                continue
            flag = 0
            for c in num:
                if i%int(c) !=0:
                    flag = 1
                    break
            if flag == 0:
                res.append(i)
        return res
        