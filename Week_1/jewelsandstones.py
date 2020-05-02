class Solution:
    def numJewelsInStones(self, J: str, S: str) -> int:
        jewels = {}
        for i in J:
            if i not in jewels:
                jewels[i] = 0
        count = 0
        for i in S:
            if i in jewels:
                count+=1
        return count
            
            
        