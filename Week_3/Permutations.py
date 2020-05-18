class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        ana = [0] * 26
        N = len(s1)
        
        for c in s1:
            ana[ord(c) - ord('a')]+= 1
            
        results = []
        for index, c in enumerate(s2):
            ana[ord(c) - ord('a')]-= 1
            
            if index>=N:
                ana[ord(s2[index-N]) - ord('a')]+= 1
            
            if index>= N-1 and all(x==0 for x in ana):
                return True
        
        return False
        