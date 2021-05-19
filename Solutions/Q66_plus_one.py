class Solution(object):
    def plusOne(self, digits):
        """
        :type digits: List[int]
        :rtype: List[int]
        """
        new_list = []
        val = digits[-1] + 1
        if val>9:
            new_list.append(val%10)
            carry = 1
        else:
            new_list.append(val)
            carry = 0
        for i in range(len(digits)-2,-1,-1):
                val = digits[i] + carry
                if val>9:
                    new_list.append(val%10)
                    carry = 1
                else:
                    new_list.append(val)
                    carry = 0
        if carry == 1:
            new_list.append(1)
        return reversed(new_list)
        