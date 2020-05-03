class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        ransom = {}
        for i in ransomNote:
            if i in ransom:
                ransom[i]+=1
            else:
                ransom[i]=1

        for i in magazine:
            if i in ransom and ransom[i]!=0:
                ransom[i]-=1
        
        return all(value == 0 for value in ransom.values())
            
                
        