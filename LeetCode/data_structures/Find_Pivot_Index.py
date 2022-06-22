# Given an array of integers nums, calculate the pivot index of this array.
#
# The pivot index is the index where the sum of all the numbers strictly to the left of the index is equal to the sum
# of all the numbers strictly to the index's right.
#
# If the index is on the left edge of the array, then the left sum is 0 because there are no elements to the left.
# This also applies to the right edge of the array.
#
# Return the leftmost pivot index. If no such index exists, return -1.
#
# Constraints:
#
#     1 <= nums.length <= 104
#     -1000 <= nums[i] <= 1000


from typing import List


def pivotIndex(nums: List[int]) -> int:
    sum_tail = sum(nums)
    sum_head = 0

    for index, num in enumerate(nums):
        sum_tail -= num
        if sum_head == sum_tail:
            return index
        sum_head += num

    return -1


def test_pivotIndex():
    assert pivotIndex([1, 7, 3, 6, 5, 6]) == 3
