class Solution:
    def firstUniqChar(self, s: str) -> int:
        uniq = {}
        for i in range(len(s)):
            if s[i] not in uniq:
                uniq[s[i]] = 1
            else:
                uniq[s[i]]-= 1
        
        for i in range(len(s)):
            if uniq[s[i]] == 1:
                return i
        return -1

        