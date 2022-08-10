# Given an array nums. We define a running sum of an array as runningSum[i] = sum(nums[0]…nums[i]).
#
# Return the running sum of nums.
#
# Constraints:
#
#     1 <= nums.length <= 1000
#     -10^6 <= nums[i] <= 10^6
#
# The problem can be solved by "accumulate()" in one line.
# However, it seems that the approach down below runs faster.

from typing import List


def runningSum(nums: List[int]) -> List[int]:
    rSum = [nums[0]]
    for i in range(1, len(nums)):
        rSum.append(rSum[i-1] + nums[i])
    return rSum


def test_runningSum():
    assert runningSum([1, 2, 3, 4]) == [1, 3, 6, 10]
