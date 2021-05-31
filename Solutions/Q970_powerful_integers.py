class Solution(object):
    def powerfulIntegers(self, x, y, bound):
        """
        :type x: int
        :type y: int
        :type bound: int
        :rtype: List[int]
        """
        res = []
        for i in range(100):
            for j in range(100):
                power = x**i + y**j
                if power <= bound:
                    res.append(power)
                else:
                    break
        return list(set(res))
                
        