class Node:
    def __init__(self, val):
        self.val = val
        self.next = None


class MyHashMap:
    def __init__(self):
        """
        Initialize your data structure here.
        """
        # use chained array
        self.cap = 10000
        self.keys = [None] * self.cap

    def put(self, key: int, value: int) -> None:
        """
        value will always be non-negative.
        """
        hash_num = key % self.cap
        if self.keys[hash_num]:
            node = self.keys[hash_num]

            while node and node.val[0] != key:
                pre = node
                node = node.next

            if not node:
                pre.next = Node((key, value))
            else:
                node.val = (key, value)
        else:
            self.keys[hash_num] = Node((key, value))

    def get(self, key: int) -> int:
        """
        Returns the value to which the specified key is mapped, or -1 if this map contains no mapping for the key
        """
        hash_num = key % self.cap
        if self.keys[hash_num]:
            node = self.keys[hash_num]
            while node and node.val[0] != key:
                node = node.next
            if node:
                return node.val[1]
        return -1

    def remove(self, key: int) -> None:
        """
        Removes the mapping of the specified value key if this map contains a mapping for the key
        """
        hash_num = key % self.cap
        if self.keys[hash_num]:
            node = self.keys[hash_num]
            pre = None
            while node and node.val[0] != key:
                pre = node
                node = node.next
            if node:
                if pre:
                    pre.next = node.next
                else:
                    self.keys[hash_num] = node.next


obj = MyHashMap()
obj.put(1, 2)
print(obj.get(10001))
print(obj.get(1))

obj.put(10001, 3)
print(obj.get(10001))
print(obj.get(1))


obj.remove(1)
print(obj.get(10001))
print(obj.get(1))
