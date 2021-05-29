class Solution(object):
    def canPlaceFlowers(self, flowerbed, n):
        """
        :type flowerbed: List[int]
        :type n: int
        :rtype: bool
        """
        if len(flowerbed)==1:
            if flowerbed[0] == 0:
                flowerbed[0] = 1
                n -= 1
            if n>0:
                return False
            return True
        
        if flowerbed[0] == 0 and flowerbed[1] == 0 and n>0:
            flowerbed[0] = 1
            n -= 1
         
        prev = flowerbed[0]
            
        for i in range(1, len(flowerbed)):
            if i==len(flowerbed)-1:
                if prev == 0 and flowerbed[i] == 0 and n > 0:
                    flowerbed[i] = 1
                    n -=1
            else:
                next_spot = flowerbed[i+1]
                #print(prev, flowerbed[i],next_spot,n)
                if prev == 0 and flowerbed[i] == 0 and next_spot == 0:
                        flowerbed[i] = 1
                        n -=1
            prev = flowerbed[i]
        if n>0:
            return False
        return True
            
        