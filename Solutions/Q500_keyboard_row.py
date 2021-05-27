class Solution(object):
    def findWords(self, words):
        """
        :type words: List[str]
        :rtype: List[str]
        """
        first_row = ['q', 'w', 'e','r','t','y','u','i','o','p']
        second_row = ['a', 's', 'd','f','g','h','j','k','l']
        third_row = ['z', 'x', 'c','v','b','n','m']
        
        def get_word_score(word):
            score = [0, 0, 0]
            for c in word:
                if c in first_row:
                    score[0] += 1
                elif c in second_row:
                    score[1] += 1
                elif c in third_row:
                    score[2] += 1
            return score
        res = []
        for word in words:
            original_word = word
            word = word.lower()
            score = get_word_score(word)
            if sum(score) == max(score):
                res.append(original_word)
        return res
            
        