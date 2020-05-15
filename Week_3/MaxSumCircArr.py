class Solution:
    def kadane(self, A):
        max_so_far =A[0]
        curr_max = A[0]
        for i in range(1,len(A)):
            curr_max = max(A[i], curr_max + A[i])
            max_so_far = max(max_so_far,curr_max) 
        return max_so_far
    
    def maxSubarraySumCircular(self, A: List[int]) -> int:
        k = self.kadane(A) 
        cs= 0
        for i in range(len(A)):
            cs+= A[i]
            A[i] = -A[i]
        cs+= self.kadane(A)
        
        if cs>k and cs!=0:
            return cs
        else:
            return k
         
        