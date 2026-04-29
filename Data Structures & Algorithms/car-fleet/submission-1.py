class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        pair = [[p,s] for p, s in zip(position, speed)] #create an array of pairs
                                #zip goes through positiona dn speed array simultaneously
        stack = []
        for p, s in sorted(pair)[::-1]: #reverse sorted order
            stack.append((target - p) / s)
            if len(stack) > 1 and stack[-1] <= stack[-2]: #collision
                stack.pop()
        return len(stack)
