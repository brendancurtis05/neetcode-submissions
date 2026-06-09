class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        count = {} #hashmap to count the occurances of each char
        res = 0 #longest substring with k replacements
        l = 0
        for r in range(len(s)):
            count[s[r]] = 1 + count.get(s[r], 0) #incrementing the occurance count of that character
            while (r-l+1) - max(count.values()) > k: #while size of our window is not valid (window size - count of highest value is our window > k)
                count[s[l]] -= 1 #decrement count of that char
                l+=1

            res = max(res, r-l + 1)
        return res
        