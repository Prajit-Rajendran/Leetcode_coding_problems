class Solution(object):
    def frequencySort(self, s):
        """
        :type s: str
        :rtype: str
        """
        freq = {}
        for c in s:
            if c not in freq.keys():
                freq[c] = 1
            else:
                freq[c] += 1
                
        freq_list = []
        for key in freq.keys():
            freq_list.append((key, freq[key]))
        freq_list = sorted(freq_list, key=lambda x: x[1], reverse=True)
        
        new_s = ''
        for (a,b) in freq_list:
            new_s = new_s + a*b
        return new_s
        