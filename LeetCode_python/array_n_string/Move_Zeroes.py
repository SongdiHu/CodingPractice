from typing import List


def moveZeroes(nums: List[int]) -> None:
    """
    Do not return anything, modify nums in-place instead.
    """
    j = 0
    for i in range(len(nums)):
        if nums[i] != 0:
            nums[i], nums[j] = nums[j], nums[i]

        if nums[j] != 0:
            j += 1


def test_moveZeroes():
    nums = [0, 1, 0, 3, 12]
    moveZeroes(nums)
    print(nums)
    assert nums == [1, 3, 12, 0, 0]


if __name__ == '__main__':
    test_moveZeroes()
