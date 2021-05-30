class Solution(object):
    def numUniqueEmails(self, emails):
        """
        :type emails: List[str]
        :rtype: int
        """
        res = []
        uniq_domains = []
        for m in emails:
            m = m.split('@')
            try:
                idx = m[0].index('+')
                m[0] = m[0][:idx]
            except:
                pass
            uniq_str = ''
            for c in m[0]:
                if c!='.':
                    uniq_str += c
            print(str(m[1]))
            uniq_domains.append(str(m[1]))
            if str(m[1]) not in uniq_domains:
                res.append(str(uniq_str) + str(m[1]))
                print(str(uniq_str) + str(m[1]))
            else:
                res.append(str(uniq_str) + '*' + str(m[1]))
                print(str(uniq_str) + '*' + str(m[1]))
        return len(list(set(res)))