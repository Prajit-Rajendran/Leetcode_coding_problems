class Solution(object):
    def numJewelsInStones(self, jewels, stones):
        """
        :type jewels: str
        :type stones: str
        :rtype: int
        """
        jewel_dict = {}
        for gem in jewels:
            if gem not in jewel_dict.keys():
                jewel_dict[gem] = 1
        count = 0
        for s in stones:
            try:
                jewel_dict[s] += 1
                count += 1
            except:
                pass
        return count
                
        