class Solution(object):
    def reverseString(self, s):
        """
        :type s: List[str]
        :rtype: None Do not return anything, modify s in-place instead.
        """
        def ceil(x):
            if x > int(x):
                return x+1
            else:
                return int(x)
            
        for i in range(ceil(len(s)/2)):
            print(s[i], s[-1 - i])
            temp = s[i]
            s[i] = s[-1 - i]
            s[-1 - i] = temp
        
        