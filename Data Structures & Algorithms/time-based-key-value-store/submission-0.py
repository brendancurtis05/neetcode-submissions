class TimeMap:

    def __init__(self):
        self.store = {} #key = string, value = [list of [value, timestamp]]
                        #ley : list of [val, timestamp]

    def set(self, key: str, value: str, timestamp: int) -> None:
        if key not in self.store:
            self.store[key] = [] #create a list if not there already
        
        self.store[key].append([value,timestamp]) #append [value, timestamp] to list at key

    def get(self, key: str, timestamp: int) -> str:
        res = ""
        values = self.store.get(key, []) #if cant find anything at key, it will return []
        
        #binary search
        l, r = 0, len(values)-1
        while l <= r:
            m = (l+r)//2
            if values[m][1] <= timestamp: #valid value
                res = values[m][0] #closest we've seen so far
                l = m+1
            else:
                r = m-1
        return res
