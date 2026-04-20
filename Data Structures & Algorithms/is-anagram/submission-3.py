class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t): #strings are not the same length
            return False
        
        countT = {} #create a hashmap for t
        countS = {} #create a hashmap for s

        for i in range(len(s)): #itterate through strings (same length as t)
            countS[s[i]] = 1 + countS.get(s[i], 0) #gets the occurences of char in S
            countT[t[i]] = 1 + countT.get(t[i], 0) #gets the occurences of char in S
        
        for c in countS:
            if countS[c] != countT.get(c, 0):
                return False

        return True