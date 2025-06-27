class DLL:
    def __init__(self,key,val=0,prev=None,next=None):
        self.key = key
        self.val = val
        self.prev = prev
        self.next = next
class LRUCache:

    def __init__(self, capacity: int):
        self.capacity = capacity
        self.lookup = {}
        self.head = DLL(-1)
        self.tail = DLL(-1)
        self.head.next = self.tail
        self.tail.prev = self.head
    def insertTail(self,node):
        tailPrev = self.tail.prev
        tailPrev.next = node
        node.prev = tailPrev
        node.next = self.tail
        self.tail.prev = node
    def removeHead(self):
        removeNode = self.head.next
        self.head.next = removeNode.next
        removeNode.next.prev = self.head
        return removeNode
    def removeNode(self,node):
        leftNode = node.prev
        rightNode = node.next
        leftNode.next = rightNode
        rightNode.prev = leftNode

    def get(self, key: int) -> int:
        if key not in self.lookup:
            return -1
        node = self.lookup[key]
        self.removeNode(node)
        self.insertTail(node)
        return node.val

    def put(self, key: int, value: int) -> None:
        if key in self.lookup:  
            node = self.lookup[key]
            self.removeNode(node)
        node = DLL(key,value)
        self.lookup[key] = node
        self.insertTail(node)
        if len(self.lookup) > self.capacity:
            node = self.head.next
            self.removeNode(node)
            del self.lookup[node.key]

        


# Your LRUCache object will be instantiated and called as such:
# obj = LRUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)