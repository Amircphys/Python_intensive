class Node():
    def __init__(self, name, val, prev=None, next=None):
        self.name = name
        self.val = val
        self.prev = prev
        self.next = next
        
    def __repr__(self):
        return f"key: {self.name}; value: {self.val}"

class LRUCache:
    def __init__(self, limit=42):
        self.dict = {}
        self.head = None
        self.tail = None
        self.limit = limit
           
    def get(self, key):
        return self.dict.get(key, None)
    
    def add_value(self, key, value):
        node = Node(key, value)
        if not self.head:
            self.head = node
        if not self.tail:
            self.tail = node
        else:
            node.prev = self.tail
            self.tail.next = node
            self.tail = node
        self.dict[key] = value
        if len(self.dict) > self.limit:
            self.remove()
    
    def remove(self):
        rm_key = self.head.name
        self.head = self.head.next
        self.dict.pop(rm_key, None)