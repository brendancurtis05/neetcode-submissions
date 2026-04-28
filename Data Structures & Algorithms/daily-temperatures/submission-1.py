class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        res = [0] * len(temperatures) #create a list of length temp
        stack = [] # pair: [temp, index]
        for i, temp in enumerate(temperatures): # go through index and temp
            while stack and temp > stack[-1][0]: #while stack is not empty and value of temp is greater than top of stack
                stackT, stackInd = stack.pop() # pop temp and index
                res[stackInd] = (i - stackInd) # add to res list the index in enumerate - stack index for that temp
            stack.append([temp, i]) #append new temp
        return res


        