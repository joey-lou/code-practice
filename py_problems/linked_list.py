from typing import List, Optional


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

    def __repr__(self) -> str:
        return f"N-{self.val}"


class Solution:
    def reverseKGroup(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        """reverse all groups that is of k size in sequence"""
        if head is None:
            return head
        root = ListNode(next=head)
        node_in_stack: List[ListNode] = []
        last_group_tail = root
        curr_node = head
        while curr_node:
            node_in_stack.append(curr_node)
            curr_node = curr_node.next
            if len(node_in_stack) == k:
                prev_stack_node = None
                while node_in_stack:
                    stack_end_node = node_in_stack.pop()
                    if prev_stack_node is None:
                        prev_stack_node = last_group_tail
                    prev_stack_node.next = stack_end_node
                    prev_stack_node = stack_end_node
                last_group_tail = stack_end_node
                last_group_tail.next = curr_node
        return root.next

    def partition(self, head: Optional[ListNode], x: int) -> Optional[ListNode]:
        greater_head = None
        greater_tail = None

        lesser_head = None
        lesser_tail = None

        curr_node = head
        while curr_node:
            if curr_node.val < x:
                if lesser_head is None:
                    lesser_head = lesser_tail = curr_node
                else:
                    lesser_tail.next = curr_node
                    lesser_tail = curr_node
            else:
                if greater_head is None:
                    greater_head = greater_tail = curr_node
                else:
                    greater_tail.next = curr_node
                    greater_tail = curr_node
            curr_node = curr_node.next
        if lesser_head is not None:
            lesser_tail.next = greater_head
            greater_tail.next = None
            return lesser_head
        return greater_head

    def isPalindrome(self, head: Optional[ListNode]) -> bool:
        if head is None:
            return True

        current_head = head

        def recurse(node):
            nonlocal current_head
            if (
                current_head != head
                and current_head == node
                or node.next == current_head
            ):
                return True
            if node.next:
                is_good = recurse(node.next)
                current_head = current_head.next
                return is_good and (current_head.val == node.val)
            else:
                return current_head.val == node.val

        return recurse(head)

    def minCut(self, s: str) -> int:
        n = len(s)
        if not n:
            return 0
        dp = [n] * (
            n + 1
        )  # at most n-1 cuts, so n is a large enough number for boundary
        dp[0] = -1
        for dp_center in range(1, n + 1):
            for dp_left_edge in range(dp_center, 0, -1):
                # start from center outwards
                radius = dp_center - dp_left_edge
                dp_right_edge = dp_center + radius
                if dp_right_edge > n:
                    break
                print(dp_left_edge, dp_center, dp_right_edge, radius)
                if s[dp_left_edge - 1] == s[dp_right_edge - 1]:
                    dp[dp_center] = min(dp[dp_center], dp[dp_left_edge - 1] + 1)
                else:
                    break
            print(dp)
            print(dp[dp_left_edge - 1])
        return dp[-1]


def list_to_llist(lst: list) -> ListNode:
    root = ListNode()
    curr_node = root
    for val in lst:
        node = ListNode(val)
        curr_node.next = node
        curr_node = node
    return root.next


def llist_to_list(llst: ListNode) -> list:
    retval = []
    node = llst
    while node is not None:
        retval.append(node.val)
        node = node.next
    return retval


if __name__ == "__main__":

    print(llist_to_list(Solution().partition(list_to_llist([1, 4, 3, 2, 5, 2]), 3)))
    print(llist_to_list(list_to_llist([1, 2, 3, 4])))
    print(Solution().isPalindrome(list_to_llist([1, 2])))
    print(Solution().minCut("aab"))
