# You are given two non-empty linked lists representing two non-negative integers. The digits are stored in reverse
# order, and each of their nodes contains a single digit. Add the two numbers and return the sum as a linked list.
#
# You may assume the two numbers do not contain any leading zero, except the number 0 itself.
#
# Constraints:
#
#     The number of nodes in each linked list is in the range [1, 100].
#     0 <= Node.val <= 9
#     It is guaranteed that the list represents a number that does not have leading zeros.


from random import randint
from typing import Optional


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


def addTwoNumbers(l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
    tmp_node = ListNode()
    output_head = tmp_node
    c = 0
    while l1 or l2:
        sum_v1_v2 = c
        if l1 is not None:
            sum_v1_v2 += l1.val
            l1 = l1.next
        if l2 is not None:
            sum_v1_v2 += l2.val
            l2 = l2.next

        tmp_node.val = sum_v1_v2 % 10
        c = sum_v1_v2 // 10

        if l1 or l2:
            tmp_node.next = ListNode()
            tmp_node = tmp_node.next

    if c > 0:
        tmp_node.next = ListNode(val=c)

    return output_head


def test_addTwoNumbers():
    l1 = ListNode()
    l1_in = l1
    l1_head = l1
    l2 = ListNode()
    l2_in = l2
    l2_head = l2

    for i in range(5):
        l1.val = randint(1, 9)
        l2.val = randint(1, 9)

        if i < 5 - 1:
            l1.next = ListNode()
            l2.next = ListNode()
            l1 = l1.next
            l2 = l2.next

    result_list = addTwoNumbers(l1_in, l2_in)

    print("\nl1: ")
    while l1_head:
        print(l1_head.val)
        l1_head = l1_head.next

    print("l2: ")
    while l2_head:
        print(l2_head.val)
        l2_head = l2_head.next

    print("result: ")
    while result_list:
        print(result_list.val)
        result_list = result_list.next


if __name__ == "__main__":
    test_addTwoNumbers()

