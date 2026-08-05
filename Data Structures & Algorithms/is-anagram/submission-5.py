class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        
        if len(s) != len(t):
            return False
        
        sSet={}
        tSet={}
        for i in range(len(s)):
            sSet[s[i]] = 1 + sSet.get(s[i], 0)
            tSet[t[i]] = 1 + tSet.get(t[i], 0)

        return sSet == tSet