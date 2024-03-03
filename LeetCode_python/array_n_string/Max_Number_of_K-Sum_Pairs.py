from typing import List


def maxOperations(nums: List[int], k: int) -> int:
    if len(nums) < 1:
        return 0
    nums = sorted(nums)
    i = 0
    j = len(nums) - 1
    num_of_hits = 0
    while i < j:
        if nums[i] + nums[j] == k:
            num_of_hits += 1
            j -= 1
            i += 1
        elif nums[i] + nums[j] > k:
            j -= 1
        else:
            i += 1

    return num_of_hits


def test_maxOperations():
    assert maxOperations([1, 2, 3, 4], 5) == 2


if __name__ == '__main__':
    test_maxOperations()
