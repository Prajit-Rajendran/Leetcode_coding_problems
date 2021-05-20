class Solution(object):
    def isHappy(self, n):
        """
        :type n: int
        :rtype: bool
        """
        if n == 1:
            return True
        if n**2 < 10:
                return False
        digits = str(n)
        visited = {}
        while 1:
            new_num = 0 
            for d in digits:
                new_num += int(d)**2
            digits = str(new_num)
            if new_num == 1:
                return True
            try:
                visited[new_num] += 1
                return False
            except:
                visited[new_num] = 1
                
            
        