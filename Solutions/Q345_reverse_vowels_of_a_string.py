class Solution(object):
    def reverseVowels(self, s):
        """
        :type s: str
        :rtype: str
        """
        vow_dict = {}
        vow_list = []
        for i in range(len(s)):
            if s[i] in ['a', 'e', 'i', 'o', 'u', 'A', 'E', 'I', 'O', 'U']:
                vow_list.append(str(s[i]))
                vow_dict[i] = 1
        
        new_s = ''
        for i in range(len(s)):
            try:
                vow_dict[i] += 1
                new_s += vow_list[-1]
                vow_list = vow_list[:-1]
            except:
                new_s += s[i]
        
        return new_s
                
                
        