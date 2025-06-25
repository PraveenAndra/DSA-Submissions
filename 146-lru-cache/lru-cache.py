class Node:
    def __init__(self,key,val):
        self.prev = None
        self.next = None
        self.val= val
        self.key = key
class LRUCache:

    def __init__(self, capacity: int):
        self.capacity = capacity
        self.lookup = {}
        self.head = Node(-1,-1)
        self.tail = Node(-1,-1)
        self.head.next= self.tail
        self.tail.prev = self.head
        

    def get(self, key: int) -> int:
        if key not in self.lookup:
            return -1
        node = self.lookup[key]
        self.remove(node)
        self.add(node)
        return node.val

    def put(self, key: int, value: int) -> None:
        if key in self.lookup:
            self.remove(self.lookup[key])
        node = Node(key,value)
        self.add(node)
        self.lookup[key] = node
        if len(self.lookup) > self.capacity:
            past = self.head.next
            self.remove(past)
            del self.lookup[past.key]

    def remove(self,node):
        prev_node = node.prev
        next_node = node.next
        prev_node.next = next_node
        next_node.prev = prev_node
    def add(self,node):
        prev_end = self.tail.prev
        prev_end.next = node
        node.next = self.tail
        node.prev = prev_end
        self.tail.prev = node


        


# Your LRUCache object will be instantiated and called as such:
# obj = LRUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)