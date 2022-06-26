# Given the head of a linked list, return the node where the cycle begins. If there is no cycle, return null.
#
# There is a cycle in a linked list if there is some node in the list that can be reached again by continuously
# following the next pointer. Internally, pos is used to denote the index of the node that tail's next pointer is
# connected to (0-indexed). It is -1 if there is no cycle. Note that pos is not passed as a parameter.
#
# Do not modify the linked list.
#
# Constraints:
#
#     The number of the nodes in the list is in the range [0, 104].
#     -105 <= Node.val <= 105
#     pos is -1 or a valid index in the linked-list.
#
# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


# Memory complexity is high. (0(n))
def detectCycle_set(head: Optional[ListNode]) -> Optional[ListNode]:
    node_set = []
    tmp_node = head
    cycle_exists = False
    while head and not cycle_exists:
        if head not in node_set:
            node_set.append(head)
            head = head.next
        else:
            cycle_exists = True
    return head


# Follow up: Can you solve it using O(1) (i.e. constant) memory?
# Apply Floyd’s Cycle Detection Algorithm/the tortoise and hare algorithm.
def detectCycle_fast_slow(head: Optional[ListNode]) -> Optional[ListNode]:
    fast = slow = head

    # Detect if cycle exists. (Them will meet eventually.)
    while fast and fast.next:
        fast = fast.next.next
        slow = slow.next

        # Found cycle!
        if fast == slow:

            # head and slow will meet at the start of cycle 100%
            # because they need the same number of steps moving to current position of slow
            # paths were branched before entering the cycle
            while head != slow:
                head = head.next
                slow = slow.next
            return head
    return None
