class Node:
    def __init__(self, value, prev=None, next=None):
        self.val = value
        self.prev = prev
        self.next = next


class LinkedList:
    # assume each value is unique
    def __init__(self, max_val: int):
        self.sentinel = Node(value=-1)
        self.sentinel.next = self.sentinel.prev = self.sentinel
        self.val_to_node = {}
        self.max_val = max_val
        self.len = 0

    def __repr__(self) -> str:
        nodes = []
        node = self.list_front
        while node and node.val != -1:
            nodes.append(f"{node.val}")
            node = node.next
        return "[" + "->".join(nodes) + "]"

    @property
    def list_front(self) -> Node:
        return self.sentinel.next

    @property
    def list_back(self) -> Node:
        return self.sentinel.prev

    @list_front.setter
    def list_front(self, node):
        self.sentinel.next = node

    @list_back.setter
    def list_back(self, node):
        self.sentinel.prev = node

    def append(self, val):
        node = Node(val)
        self.val_to_node[val] = node
        self._append(node)

    def _append(self, node: Node):
        back_node = self.list_back
        back_node.next, node.prev, node.next = node, back_node, self.sentinel
        self.list_back = node
        self.len += 1

    def prepend(self, val):
        node = Node(val)
        self.val_to_node[val] = node
        self._prepend(node)

    def _prepend(self, node: Node):
        front_node = self.list_front
        front_node.prev, node.next, node.prev = node, front_node, self.sentinel
        self.list_front = node
        self.len += 1

    def pop(self, val):
        node = self.val_to_node[val]
        del self.val_to_node[val]
        node.prev.next, node.next.prev = node.next, node.prev
        self.len -= 1

    def insert_ordered(self, val):
        next_node = self.list_front
        while next_node.val != -1 and next_node.val <= val:
            next_node = next_node.next

        prev_node = next_node.prev
        node = Node(val, prev_node, next_node)
        prev_node.next, next_node.prev = node, node
        self.val_to_node[val] = node
        self.len += 1

    def get_next_number(self):
        if self.len == 0:
            return 0  # always the first index

        # handle first interval
        if self.list_front.val != 0:
            best_distance = self.list_front.val
            best_val = 0
        else:
            best_distance = 0
            best_val = None

        prev_node = self.list_front
        next_node = prev_node.next
        while next_node and next_node.val != -1:
            i, j = prev_node.val, next_node.val
            if j > i + 1:
                distance = (j - i) // 2
                if distance > best_distance:
                    best_distance = distance
                    best_val = i + distance
            prev_node, next_node = next_node, next_node.next

        # can potentially assign the last index
        if self.list_back.val != self.max_val:
            if self.max_val - self.list_back.val > best_distance:
                best_val = self.max_val
        return best_val


llst = LinkedList(9)


for i in range(4):
    print(llst.get_next_number())
    llst.insert_ordered(llst.get_next_number())
    print(llst)

llst.pop(4)
print(llst)

print(llst.get_next_number())
llst.insert_ordered(llst.get_next_number())
print(llst)
# for i in range(3):
#     print(llst.get_next_number())
#     llst.insert_ordered(llst.get_next_number())
#     print(llst)

# llst.pop(15)
# print(llst.get_next_number())
# llst.insert_ordered(llst.get_next_number())
# print(llst)

# llst.pop(20)
# llst.pop(0)
# print(llst.get_next_number())
# llst.insert_ordered(llst.get_next_number())
# print(llst)

# print(llst.get_next_number())
# llst.insert_ordered(llst.get_next_number())
# print(llst)

# print(llst.get_next_number())
# llst.insert_ordered(llst.get_next_number())
# print(llst)
