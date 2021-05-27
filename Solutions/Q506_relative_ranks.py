class Solution(object):
    def findRelativeRanks(self, score):
        """
        :type score: List[int]
        :rtype: List[str]
        """
        score_sort = sorted(score, reverse=True)
        ranks = []
        rank_list = ["Gold Medal","Silver Medal","Bronze Medal","4","5"]
        for s in score:
            idx = score_sort.index(s)
            if idx == 0:
                ranks.append("Gold Medal")
            elif idx == 1:
                ranks.append("Silver Medal")
            elif idx == 2:
                ranks.append("Bronze Medal")
            else:
                ranks.append(str(idx+1))
        return ranks