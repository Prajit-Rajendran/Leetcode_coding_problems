class Solution(object):
    def fizzBuzz(self, n):
        """
        :type n: int
        :rtype: List[str]
        """
        string = []
        for elem in range(1, n+1):
            if elem%15 == 0:
                string.append("FizzBuzz")
            elif elem%3 == 0:
                string.append("Fizz")
            elif elem%5 == 0:
                string.append("Buzz")
            else:
                string.append(str(elem))
        return string