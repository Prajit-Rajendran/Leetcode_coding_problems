class Solution(object):
    def trailingZeroes(self, n):
        """
        :type n: int
        :rtype: int
        """
        if n==0:
            return 0
        
        def factorial(n):
            if n==1:
                return 1
            return n*factorial(n-1)
        
        fact = str(factorial(n))
        count = 0
        for i in range(1, len(fact)+1):
            if fact[-i]=='0':
                count += 1
            elif fact[-i]!='0':
                return count
        return count
        
        