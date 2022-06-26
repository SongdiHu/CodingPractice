# Given the head of a singly linked list, return the middle node of the linked list.
#
# If there are two middle nodes, return the second middle node.
#
# Constraints:
#
#     The number of nodes in the list is in the range [1, 100].
#     1 <= Node.val <= 100
#
# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


from typing import Optional


def middleNode(head: Optional[ListNode]) -> Optional[ListNode]:
    def rec_middleNode(curr_node, pos):
        if curr_node.next:
            mid_node, mid_pos = rec_middleNode(curr_node.next, pos + 1)
            if pos == mid_pos:
                return curr_node, pos
            else:
                return mid_node, mid_pos
        else:
            return curr_node, (pos >> 1) + 1

    return rec_middleNode(head, 1)[0]


def test_middleNode():
    list1_vals = [1, 2, 3, 4, 5]

    list1 = ListNode()
    list1_head = list1

    for val in list1_vals:
        tmp_node = ListNode(val)
        list1.next = tmp_node
        list1 = list1.next

    list1_head = list1_head.next

    final_list = middleNode(list1_head)

    while final_list:
        print(final_list.val)
        final_list = final_list.next


test_middleNode()
