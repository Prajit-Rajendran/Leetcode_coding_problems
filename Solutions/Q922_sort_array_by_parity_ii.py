class Solution(object):
    def sortArrayByParityII(self, A):
        """
        :type A: List[int]
        :rtype: List[int]
        """
        even_idx = []
        odd_idx = []
        for i in range(len(A)):
            if i%2 == 0 and A[i]%2 == 1:
                even_idx.append(i)
            if i%2 == 1 and A[i]%2 == 0:
                odd_idx.append(i)
                
        for i in range(len(odd_idx)):
            temp = A[odd_idx[i]]
            A[odd_idx[i]] = A[even_idx[i]]
            A[even_idx[i]] = temp
            
        return A
            
        