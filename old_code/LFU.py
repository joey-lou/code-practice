import collections


class Node:
    def __init__(self, key, value):
        self.key = key
        self.val = value
        self.freq = 0
        self.prev = self.next = None


class DLinkedList:
    def __init__(self):
        self.head = Node(None, None)
        self.tail = Node(None, None)
        self.head.next, self.tail.prev = self.tail, self.head
        self.size = 0

    def append(self, node):
        prev = self.tail.prev
        node.prev, self.tail.prev, prev.next, node.next = prev, node, node, self.tail
        self.size += 1

    def pop(self, node):
        prev, follow = node.prev, node.next
        prev.next, follow.prev = follow, prev
        self.size -= 1

    def popfirst(self):
        node = self.head.next
        self.head.next, node.next.prev = node.next, self.head
        self.size -= 1
        return node


class LFUCache:
    def __init__(self, capacity: int):
        self.nodes = {}
        self.freq = collections.defaultdict(DLinkedList)
        self.cap = capacity
        self.minfreq = 0

    def get(self, key: int) -> int:
        if key not in self.nodes:
            return -1

        node = self.nodes[key]
        self.freq[node.freq].pop(node)
        node.freq += 1
        self.freq[node.freq].append(node)
        if self.freq[node.freq - 1].size == 0:
            self.minfreq = node.freq
        return node.val

    def pop(self):
        freq = self.minfreq
        node = self.freq[freq].popfirst()
        del self.nodes[node.key]

    def put(self, key: int, value: int) -> None:
        if key in self.nodes:
            node = self.nodes[key]
            self.freq[node.freq].pop(node)
            node.freq += 1
            self.freq[node.freq].append(node)
            if self.freq[node.freq - 1].size == 0:
                self.minfreq = node.freq
            node.val = value
        else:
            if self.cap == len(self.nodes):
                self.pop()
            node = Node(key, value)
            self.freq[0].append(node)
            self.nodes[key] = node
            self.minfreq = 0


x = DLinkedList()
a = Node(1, 2)
x.append(a)
print(x.head.next == a, x.head.next.next == x.tail, x.size)
x.popfirst()
print(x.head.next == x.tail)
print(x.size)
# Your LFUCache object will be instantiated and called as such:
# obj = LFUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)
