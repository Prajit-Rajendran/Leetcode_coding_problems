class Solution(object):
    def isAlienSorted(self, words, order):
        """
        :type words: List[str]
        :type order: str
        :rtype: bool
        """
        order_dict = {}
        i = 0
        for c in order:
            if c not in order_dict.keys():
                order_dict[str(c)] = i
                i += 1
        
        print(order_dict)
        for i in range(1, len(words)):
            prev_word = words[i-1]
            cur_word = words[i]
            flag = 0
            for j in range(min(len(prev_word), len(cur_word))):
                if order_dict[prev_word[j]] < order_dict[cur_word[j]] and flag == 0:
                    flag = -1
                elif order_dict[prev_word[j]] > order_dict[cur_word[j]] and flag == 0:
                    flag = 1
                #print(prev_word[j], order_dict[prev_word[j]], cur_word[j], order_dict[cur_word[j]], flag)
            print(prev_word, cur_word, flag)
            if flag == 1:
                return False
            if flag == 0:
                if len(prev_word) > len(cur_word):
                    return False
        return True

                
                
        