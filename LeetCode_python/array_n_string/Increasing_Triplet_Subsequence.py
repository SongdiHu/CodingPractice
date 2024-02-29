import math
from typing import List


def increasingTriplet(nums: List[int]) -> bool:
    if len(nums) < 3:
        return False
    min_most = nums[0]
    min_sec_most = math.inf
    min_most_cand = min_most
    for i in range(1, len(nums)):
        if min_sec_most is not math.inf:
            if nums[i] > min_sec_most:
                return True
            else:
                if min_most < nums[i] < min_sec_most:
                    min_sec_most = nums[i]
                elif min_most_cand < nums[i] <= min_sec_most:
                    min_most = min_most_cand
                    min_sec_most = nums[i]
                elif nums[i] < min_most:
                    min_most_cand = nums[i]
        else:
            if nums[i] > min_most:
                min_sec_most = nums[i]
            elif nums[i] < min_most:
                min_most = nums[i]
    return False


def test_increasingTriplet():
    assert increasingTriplet([1, 2, 3, 4, 5]) is True
    assert increasingTriplet([5, 4, 3, 2, 1]) is False
    assert increasingTriplet([2, 1, 5, 0, 4, 6]) is True
    assert increasingTriplet([20, 100, 10, 12, 5, 13]) is True


if __name__ == '__main__':
    test_increasingTriplet()
