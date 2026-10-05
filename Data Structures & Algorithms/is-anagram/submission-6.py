class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        
        CountT = {}
        CountS = {}

        for i in range(len(s)):
            CountT[t[i]] = 1 + CountT.get(t[i], 0)
            CountS[s[i]] = 1 + CountS.get(s[i], 0)
        
        if CountT == CountS:
            return True
        return False