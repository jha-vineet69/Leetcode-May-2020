class Solution:
    def findAnagrams(self, s: str, p: str) -> List[int]:
        ana = [0] * 26
        N = len(p)
        
        for c in p:
            ana[ord(c) - ord('a')]+= 1
            
        results = []
        for index, c in enumerate(s):
            ana[ord(c) - ord('a')]-= 1
            
            if index>=N:
                ana[ord(s[index-N]) - ord('a')]+= 1
            
            if index>= N-1 and all(x==0 for x in ana):
                results.append(index - (N-1))
        
        return results