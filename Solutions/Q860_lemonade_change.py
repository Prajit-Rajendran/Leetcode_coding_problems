class Solution(object):
    def lemonadeChange(self, bills):
        """
        :type bills: List[int]
        :rtype: bool
        """
        buffer = {5: 0, 10: 0, 20: 0}
        for elem in bills:
            print(elem, buffer)
            if elem == 5:
                buffer[5] += 1
            if elem == 10:
                buffer[10] += 1
                if buffer[5] == 0:
                    return False
                buffer[5] -= 1
            if elem == 20:
                buffer[20] += 1
                if buffer[5] == 0:
                    return False
                if buffer[10] == 0 and buffer[5]<3:
                    return False
                if buffer[10] == 0 and buffer[5]>=3:
                    buffer[5] -= 3
                else:
                    buffer[5] -= 1
                    buffer[10] -= 1
        return True