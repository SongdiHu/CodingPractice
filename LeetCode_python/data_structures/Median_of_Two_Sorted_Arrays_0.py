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


from math import inf
from typing import List

def findMedianSortedArrays(nums1: List[int], nums2: List[int]) -> float:
    nums1_length = len(nums1)
    nums2_length = len(nums2)
    total_length = nums1_length + nums2_length
    mid_cand_0 = float(-inf)
    mid_cand_1 = float(-inf)
    nums1_ind = 0
    nums2_ind = 0

    for i in range(int(total_length / 2) + 1):
        mid_cand_0 = mid_cand_1
        if nums1_ind < nums1_length and nums2_ind < nums2_length:
            if nums1[nums1_ind] <= nums2[nums2_ind]:
                mid_cand_1 = nums1[nums1_ind]
                nums1_ind += 1
            else:
                mid_cand_1 = nums2[nums2_ind]
                nums2_ind += 1
        else:
            if nums1_ind < nums1_length:
                mid_cand_1 = nums1[nums1_ind]
                nums1_ind += 1
            else:
                mid_cand_1 = nums2[nums2_ind]
                nums2_ind += 1

    if total_length % 2 == 1:
        return mid_cand_1
    else:
        return (mid_cand_0 + mid_cand_1) / 2


def test_findMedian():
    assert findMedianSortedArrays([1, 3], [2]) == 2
    assert findMedianSortedArrays([1, 2], [3]) == 2
    assert findMedianSortedArrays([1, 3], [2, 4]) == 2.5
    assert findMedianSortedArrays([1, 2], [3, 4]) == 2.5
    assert findMedianSortedArrays([2], [1, 3]) == 2
    assert findMedianSortedArrays([1], [2, 3]) == 2


if __name__ == "__main__":
    test_findMedian()
