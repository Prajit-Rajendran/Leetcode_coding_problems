import math
class Solution(object):
    def climbStairs(self, n):
        """
        :type n: int
        :rtype: int
        """
        solns = []
        for x in range(n+1):
            for y in range(n+1):
                if 2*x == n - y:
                    solns.append((x,y))
        print(solns)
        count = 0
        for (a,b) in solns:
            if a==0 or b==0:
                count += 1
            else:
                num = a+b
                count += math.factorial(num)/(math.factorial(num-a)*math.factorial(a))
        return count
                    
        