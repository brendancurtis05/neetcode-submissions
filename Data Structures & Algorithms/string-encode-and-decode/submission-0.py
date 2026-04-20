class Solution:

    def encode(self, strs: List[str]) -> str:
        res = "" #result string
        for s in strs: #for strings in list
            res+=str(len(s))+ "#" + s #append length,special char,string
        
        return res #return new string

    def decode(self, s: str) -> List[str]:
        res = [] #result list
        i=0 #count

        while i < len(s): #while count is less that the fed in string
            j=i #both point to the same place
            while s[j] != '#': #increment j until it equals our special character
                j+=1
            length = int(s[i:j]) #slice the string from i to j, grabbing the number
            i = j+1 #move i past the special character
            j = i+length #move j to the end of the word
            res.append(s[i:j]) #append the sliced word
            i=j #set i pointer to j
        
        return res