class Node: #double linked list node structure
    def __init__(self, key, val):
        self.key, self.val = key, val
        self.prev = self.next = None


class LRUCache:

    def __init__(self, capacity: int):
        self.cap = capacity
        self.cache = {} #hashmap, {key : node}

        #dummy nodes for the left (least used node) and right (most recently used node)
        self.left, self.right = Node(0, 0), Node(0, 0)
        self.left.next, self.right.prev = self.right, self.left
    
    #helper funcitons
    #remove from list
    def remove(self, node):
        prev, nxt = node.prev, node.next
        prev.next, nxt.prev = nxt, prev


    #insert at right
    def insert(self, node):
        prev, nxt = self.right.prev, self.right
        prev.next = nxt.prev = node
        node.next, node.prev = nxt, prev



    def get(self, key: int) -> int:
        if key in self.cache:
            #update to most recent
            self.remove(self.cache[key]) #remove
            self.insert(self.cache[key]) #insert
            return self.cache[key].val #return value at key
        return -1


    def put(self, key: int, value: int) -> None:
        if key in self.cache: #if key in cache
            self.remove(self.cache[key]) #remove
        self.cache[key] = Node(key, value) #create new node
        self.insert(self.cache[key]) #insert

        if len(self.cache) > self.cap:
            #remove and delete least used node
            lru = self.left.next
            self.remove(lru)
            del self.cache[lru.key]
        
