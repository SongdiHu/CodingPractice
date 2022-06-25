# You are given the heads of two sorted linked lists list1 and list2.
#
# Merge the two lists in a one sorted list. The list should be made by splicing together the nodes of the first two
# lists.
#
# Return the head of the merged linked list.
#
# Constraints:
#
#     The number of nodes in both lists is in the range [0, 50].
#     -100 <= Node.val <= 100
#     Both list1 and list2 are sorted in non-decreasing order.
#
# Definition for singly-linked list.


from typing import Optional


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


def mergeTwoLists(list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
    if not list1 and not list2:
        return None
    elif not list1 or not list2:
        return list1 if list1 else list2

    if list1.val <= list2.val:
        prev_node = list1
        list1 = list1.next
    else:
        prev_node = list2
        list2 = list2.next

    final_list = prev_node

    while list1 or list2:
        if not list1 or not list2:
            prev_node.next = list1 if not list2 else list2
            list1, list2 = None, None
            continue

        if list1.val <= list2.val:
            prev_node.next = list1
            prev_node = prev_node.next
            list1 = list1.next
        else:
            prev_node.next = list2
            prev_node = prev_node.next
            list2 = list2.next

    return final_list


def test_mergeTwoLists():
    list1_vals = [1,2,3]
    list2_vals = [1,3,4]

    list1 = ListNode()
    list1_head = list1
    list2 = ListNode()
    list2_head = list2

    for val in list1_vals:
        tmp_node = ListNode(val)
        list1.next = tmp_node
        list1 = list1.next

    for val in list2_vals:
        tmp_node = ListNode(val)
        list2.next = tmp_node
        list2 = list2.next

    final_list = mergeTwoLists(list1_head.next, list2_head.next)

    while final_list:
        print(final_list.val)
        final_list = final_list.next


test_mergeTwoLists()