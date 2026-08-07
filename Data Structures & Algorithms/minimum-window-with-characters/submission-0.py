class Solution:
    def minWindow(self, s: str, t: str) -> str:
        #edge case
        if t=="": return ""

        countT, window = {}, {}

        #initialize T map
        for c in t: #for char in string t
            countT[c] = 1 + countT.get(c, 0) 
            #get will return either countT[c] or 0 if there's nothing there yet
        
        res, resLen = [-1,-1], float("infinity")
        l=0
        have, need = 0, len(countT) #have 0 of the chracters we need, len(countT) gives us the unique characters in countT

        #iterate through every char in S
        for r in range(len(s)): #r = right pointer
            c = s[r]
            window[c] = 1 + window.get(c, 0)

            #does this count satisfy what we're looking for?
            if c in countT and window[c] == countT[c]:
                have += 1
            
            #if we've met the correct have to need
            while have == need:
                if (r-l+1) < resLen:
                    res = [l,r]
                    resLen = (r-l+1)
                
                #pop from left of our window to minimize
                window[s[l]] -= 1
                if s[l] in countT and window[s[l]] < countT[s[l]]:
                    have -= 1
                l+=1
        
        l, r = res
        return s[l:r+1] if resLen != float("infinity") else ""
