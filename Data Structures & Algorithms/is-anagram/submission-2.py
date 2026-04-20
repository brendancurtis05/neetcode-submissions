class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        
        countT = {}
        countS = {}

        for i in range(len(s)):
            countS[s[i]] = 1 + countS.get(s[i], 0) #gets the occurences of char in S
            countT[t[i]] = 1 + countT.get(t[i], 0) #gets the occurences of char in S
        
        for c in countS:
            if countS[c] != countT.get(c, 0):
                return False

        return True

