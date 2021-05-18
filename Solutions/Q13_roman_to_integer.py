class Solution(object):
    def romanToInt(self, s):
        """
        :type s: str
        :rtype: int
        """
        flag = 0
        int_val = 0
        vals = {'I':1, 'V':5, 'X':10, 'L':50, 'C':100, 'D':500, 'M':1000}
        for i in range(len(s)):
            if flag == 0:
                cur_sym = s[i]
                try:
                    next_sym = s[i+1]
                    flag = 1
                    if cur_sym+next_sym == 'IV':
                        int_val += 4
                    elif cur_sym+next_sym == 'IX':
                        int_val += 9
                    elif cur_sym+next_sym == 'XL':
                        int_val += 40
                    elif cur_sym+next_sym == 'XC':
                        int_val += 90
                    elif cur_sym+next_sym == 'CD':
                        int_val += 400
                    elif cur_sym+next_sym == 'CM':
                        int_val += 900
                    else:
                        flag = 0
                        int_val += vals[cur_sym]
                except:
                    int_val += vals[cur_sym]
            else:
                flag = 0
                pass
            print(int_val)
        return int_val
                    
                        
                        
            
        