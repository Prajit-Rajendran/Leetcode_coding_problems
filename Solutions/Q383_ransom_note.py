class Solution(object):
    def canConstruct(self, ransomNote, magazine):
        """
        :type ransomNote: str
        :type magazine: str
        :rtype: bool
        """
        rans_dict = {}
        for elem in ransomNote:
            if elem not in rans_dict.keys():
                rans_dict[elem] = 1
            else:
                rans_dict[elem] += 1
        mag_dict = {}
        for elem in magazine:
            if elem not in mag_dict.keys():
                mag_dict[elem] = 1
            else:
                mag_dict[elem] += 1
        for elem in rans_dict.keys():
            try:
                if rans_dict[elem] > mag_dict[elem]:
                    return False
            except:
                return False
        return True
            
        