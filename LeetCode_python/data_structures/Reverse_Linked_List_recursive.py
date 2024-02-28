# Given the head of a singly linked list, reverse the list, and return the reversed list.
#
# Constraints:
#
#     The number of nodes in the list is the range [0, 5000].
#     -5000 <= Node.val <= 5000
#
# Follow up: A linked list can be reversed either iteratively or recursively. Could you implement both?
#
# Definition for singly-linked list.


from typing import Optional


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


def reverseList(head: Optional[ListNode]) -> Optional[ListNode]:
    if head is None:
        return None
    prev_node, final_list = _reverseList(head)
    prev_node.next = None
    return final_list


def _reverseList(head: Optional[ListNode]):
    if head.next is not None:
        prev_node, final_list = _reverseList(head.next)
        prev_node.next = head
        return head, final_list
    else:
        return head, head


def test_reverseList():
    list1_vals = [1, 2, 3]

    list1 = ListNode()
    list1_head = list1

    for val in list1_vals:
        tmp_node = ListNode(val)
        list1.next = tmp_node
        list1 = list1.next

    list1_head = list1_head.next

    final_list = reverseList(list1_head)

    while final_list:
        print(final_list.val)
        final_list = final_list.next


test_reverseList()
