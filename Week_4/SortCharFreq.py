from collections import Counter
class Solution:
    def frequencySort(self, s: str) -> str:
        counter = Counter(s)
        result = ''
        
        p = sorted(counter, key= lambda x: counter[x], reverse=True)
        
        for ch in p:
            result+=ch*counter[ch]

        return result

#Simpler but not recommended in Interview
from collections import Counter
class Solution:
    def frequencySort(self, s: str) -> str:
        counter = Counter(s)
        output = "".join(char * freq for char, freq in counter.most_common())
        return output
        
            
        