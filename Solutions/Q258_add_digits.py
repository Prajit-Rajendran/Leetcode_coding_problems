class Solution(object):
    def addDigits(self, num):
        """
        :type num: int
        :rtype: int
        """
        if num >=0 and num <=9:
            return num
        digits = str(num)
        while 1:
            sum_digits = 0
            for i in range(len(digits)):
                sum_digits += int(digits[i])
            if sum_digits >=0 and sum_digits <=9:
                return sum_digits
            digits = str(sum_digits)  
        