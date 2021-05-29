class Solution(object):
    def isOneBitCharacter(self, bits):
        """
        :type bits: List[int]
        :rtype: bool
        """
        if len(bits) == 1:
            return True
    
        if len(bits) == 2:
            if bits[0]!=1:
                return True
            else:
                return False
        
        flag = 0
        chars = []
        for i in range(len(bits)):
            if flag == 1:
                flag = 0
                continue
            if bits[i] == 1:
                chars.append(str(bits[i]) + str(bits[i+1]))
                flag = 1
            else:
                chars.append('0')
        
        print(chars)
        if chars[-1] == '0':
            return True
        return False
                
            
            
            
                
            
            
        