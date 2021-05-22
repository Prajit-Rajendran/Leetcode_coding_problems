class Solution(object):
    def isPerfectSquare(self, num):
        """
        :type num: int
        :rtype: bool
        """
        if num < 1000:
            if num in [1, 4, 9, 16, 25, 36, 49, 64, 81, 100, 121, 144, 169, 225, 256, 289, 324, 361, 400, 441, 484, 529, 576, 625, 676, 729, 784, 841, 900, 961 ]:
                return True
            return False
        digits = str(num)
        
        def digital_root(digits):
            root = 0
            for d in digits:
                root += int(d)
            return root
        
        roots = digital_root(digits)
        while roots >= 10:
            new_digits = str(roots)
            roots = digital_root(new_digits)
        if roots not in [1, 4, 7, 9]:
            return False
        if digits[-1] in ['2', '3', '7', '8']:
            print('Case 1')
            return False
        if digits[-1] == '6' and int(digits[-2])%2==0:
            print('Case 2')
            return False
        if digits[-1] != '6' and int(digits[-2])%2==1:
            print('Case 3')
            return False
        if digits[-1] == '5' and digits[-2] != '2':
            print('Case 4')
            return False
        if int(digits[-1])%2==0 and int(digits[-2])%2==0 and int(digits[-2] + digits[-1])%4!=0:
            print('Case 5')
            return False
        return True
        