# Given two sorted arrays nums1 and nums2 of size m and n respectively, return the median of the two sorted arrays.
#
# The overall run time complexity should be O(log (m+n)).
#
# Constraints:
#
#     nums1.length == m
#     nums2.length == n
#     0 <= m <= 1000
#     0 <= n <= 1000
#     1 <= m + n <= 2000
#     -106 <= nums1[i], nums2[i] <= 106


from typing import List


def findMedianSortedArrays(nums1: List[int], nums2: List[int]) -> float:
    nums = nums1 + nums2
    nums.sort()
    return (nums[len(nums) >> 1] + nums[(len(nums) - 1) >> 1]) / 2.0


def test_findMedian():
    assert findMedianSortedArrays([1, 3], [2]) == 2
    assert findMedianSortedArrays([1, 2], [3]) == 2
    assert findMedianSortedArrays([1, 3], [2, 4]) == 2.5
    assert findMedianSortedArrays([1, 2], [3, 4]) == 2.5
    assert findMedianSortedArrays([2], [1, 3]) == 2
    assert findMedianSortedArrays([1], [2, 3]) == 2


if __name__ == "__main__":
    test_findMedian()
