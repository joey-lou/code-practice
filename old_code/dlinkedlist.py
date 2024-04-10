import collections


class Node:
    def __init__(self, val):
        self.val = val
        self.prev = None
        self.next = None


class DLinkedList:
    def __init__(self):
        self.head = Node(None)
        self.tail = Node(None)
        self.head.next, self.tail.prev = self.tail, self.head

    def insert_front(self, node, prev):
        # insert node into list, given the previous node
        next = prev.next
        node.prev, node.next, prev.next, next.prev = prev, next, node, node

    def insert_back(self, node, next):
        prev = next.prev
        node.prev, node.next, prev.next, next.prev = prev, next, node, node

    def remove_node(self, node):
        # remove given node from list
        prev = node.prev
        next = node.next
        prev.next, next.prev = next, prev

    def return_first(self):
        # return -1 if no such node exists
        node = self.head.next
        if not node:
            return -1
        return node.val

    def return_last(self):
        node = self.tail.prev
        if not node:
            return -1
        return node.val

    @staticmethod
    def print(dlist):
        node = dlist.head
        print("[", end="")
        while node:
            print(node.val, end=" ")
            node = node.next
        print("]")


class AllOne:
    def __init__(self):
        """
        Initialize your data structure here.
        """

        # hashmap from key to value
        self.key_val = {}
        # map from value to key
        self.val_key = collections.defaultdict(set)
        self.val_node = {}  # value mapped to node in dlist
        self.dlist = DLinkedList()

    def update_val(self, val, new_val):
        # special case when new_val is 1
        if new_val == 1 and 1 not in self.val_node:
            node = Node(1)
            self.dlist.insert_front(node, self.dlist.head)
            self.val_node[1] = node

        if new_val != 0 and new_val not in self.val_node:
            # add new node to dlist
            node = Node(new_val)
            if val < new_val:
                prev = self.val_node[val]
                self.dlist.insert_front(node, prev)
            else:
                next = self.val_node[val]
                self.dlist.insert_back(node, next)
            self.val_node[new_val] = node

        if not self.val_key[val] and val != 0:
            # we need to remove val from dlist and map
            # if we no longer house any keys at that value
            node = self.val_node[val]
            self.dlist.remove_node(node)
            del self.val_node[val]

    def inc(self, key: str) -> None:
        """
        Inserts a new key <Key> with value 1. Or increments an existing key by 1.
        """
        # DLinkedList.print(self.dlist)
        # print(self.val_node)
        if key not in self.key_val:
            val = 1
            self.key_val[key] = val
            self.val_key[val].add(key)
            self.update_val(0, 1)

        else:
            val = self.key_val[key]
            self.key_val[key] += 1
            # update value to key
            self.val_key[val].remove(key)
            new_val = val + 1
            self.val_key[new_val].add(key)
            self.update_val(val, new_val)

    def dec(self, key: str) -> None:
        """
        Decrements an existing key by 1. If Key's value is 1, remove it from the data structure.
        """
        if key not in self.key_val:
            return
        val = self.key_val[key]

        # remove current
        self.val_key[val].remove(key)
        new_val = val - 1
        if new_val > 0:
            # if val > 1, add key to the new_val
            self.val_key[new_val].add(key)
            self.key_val[key] -= 1
        else:
            del self.key_val[key]

        self.update_val(val, new_val)

    def getMaxKey(self) -> str:
        """
        Returns one of the keys with maximal value.
        """
        largest = self.dlist.tail.prev.val
        if not largest:
            return ""
        return next(iter(self.val_key[largest]))

    def getMinKey(self) -> str:
        """
        Returns one of the keys with Minimal value.
        """
        smallest = self.dlist.head.next.val
        if not smallest:
            return ""
        return next(iter(self.val_key[smallest]))


# Your AllOne object will be instantiated and called as such:
obj = AllOne()
obj.inc("a")
obj.inc("b")
obj.inc("b")
obj.inc("b")
obj.inc("c")
obj.inc("c")
obj.dec("b")
obj.dec("a")
obj.dec("a")
obj.dec("b")
obj.dec("b")
obj.dec("b")

param_3 = obj.getMaxKey()
param_4 = obj.getMinKey()

print(param_3)
print(param_4)
