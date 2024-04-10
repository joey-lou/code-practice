# create binary tree from array
class Node:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None

    @staticmethod
    def inorder_print(node):
        if node:
            Node.inorder_print(node.left)
            print(node.val, end=",")
            Node.inorder_print(node.right)


def add(head, node):
    if node.val <= head.val:
        if not head.left:
            head.left = node
            return
        else:
            add(head.left, node)
    else:
        if not head.right:
            head.right = node
            return
        else:
            add(head.right, node)


def arr2bst(arr):
    head = Node(arr[0])
    for num in arr[1:]:
        new_node = Node(num)
        add(head, new_node)

    return head


bst = arr2bst([1, 3, 8, 4, 6, 7, 10, 11, 13])


# def in_order_print(tree):
#     if tree:
#         in_order_print(tree.left)
#         print(tree.val, end=',')
#         in_order_print(tree.right)

# in_order_print(bst)

Node.inorder_print(bst)
