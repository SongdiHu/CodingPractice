# Given an array of integers nums and an integer target, return indices of the two numbers such that they add up to
# target.
#
# You may assume that each input would have exactly one solution, and you may not use the same element twice.
#
# You can return the answer in any order.
#
# Constraints:
#
#     2 <= nums.length <= 104
#     -109 <= nums[i] <= 109
#     -109 <= target <= 109
#     Only one valid answer exists.


from typing import List


def twoSum(nums: List[int], target: int) -> List[int]:
    nums_length = len(nums)
    for i in range(nums_length - 1):
        for j in range(i + 1, nums_length):
            if target - nums[i] == nums[j]:
                return [i, j]


def test_twoSum():
    assert twoSum([2, 7, 11, 15], 9) == [0, 1] or twoSum([2, 7, 11, 15], 9) == [1, 0]
    assert twoSum([2, 7], 9) == [0, 1] or twoSum([2, 7], 9) == [1, 0]


if __name__ == "__main__":
    test_twoSum()
