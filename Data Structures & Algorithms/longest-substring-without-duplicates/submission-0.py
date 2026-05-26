class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        if s is None:
            return 0

        charSet = set() #create an empty set
        l = 0 #left pointer
        res = 0

        for r in range(len(s)): #iterate through each char via r pointer
            while s[r] in charSet: #while the character in our charSet (this means we've seen the character before)
                charSet.remove(s[l]) #remove character at left pointer
                l+=1 #increment left pointer
            charSet.add(s[r]) #add character at r to charSet
            res = max(res, r-l+1) #result = max of current result or length of our current substring
        return res


        """
        abcabcbb
        l = 0. res = 0
        r = 0, a not in subset, add to subset, return max(0, 0-0+1) = 1
        r = 1, b not in subset, add to subset, return max(1, 1-0+1) = 2
        r = 2, c not in subset, add to subset, return max(2, 2-0+1) = 3
        r = 3, a IN subset, remove s[l] = a, l+=1, return max(3, 3-1+1) = 3
        ....
        """