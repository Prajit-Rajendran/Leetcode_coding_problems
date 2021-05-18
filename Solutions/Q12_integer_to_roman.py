class Solution(object):
    def intToRoman(self, num):
        """
        :type num: int
        :rtype: str
        """
        num_str = str(num)
        factor = 1
        val_list = []
        for i in range(len(num_str)-1, -1, -1):
            val_list.append(factor*int(num_str[i]))
            factor *= 10
        val_list = sorted(val_list, reverse=True)
        rom_dict = {1:'I', 2:'II', 3:'III', 4:'IV', 5:'V', 6:'VI', 7:'VII', 8:'VIII',9:'IX', 10:'X', 20:'XX', 30:'XXX', 40:'XL', 50:'L', 60:'LX', 70:'LXX', 80:'LXXX',90:'XC', 100:'C', 200:'CC', 300:'CCC', 400:'CD', 500:'D', 600:'DC', 700:'DCC', 800:'DCCC',900:'CM', 1000:'M', 2000:'MM', 3000:'MMM'}
        print(val_list)
        rom_list = ''
        for elem in val_list:
            if elem!=0:
                rom_list = rom_list + rom_dict[elem]
        return rom_list
        