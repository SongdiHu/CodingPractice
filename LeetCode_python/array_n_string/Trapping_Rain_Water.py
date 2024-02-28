# Given n non-negative integers representing an elevation map where the width of each bar is 1, compute how much water it can trap after raining.
from typing import List


def trap(height: List[int]) -> int:
    tmp_trap = 0
    max_value = max(height)
    max_pos = height.index(max_value)
    if len(height) < 3:
        return 0

    if 0 < max_pos < len(height) - 1:
        if len(height[:max_pos + 1]) > 2:
            tmp_trap += trap(height[:max_pos + 1])
        if len(height[max_pos:]) > 2:
            tmp_trap += trap(height[max_pos:])
    else:
        sub_max = -1
        if max_pos == 0:
            sub_max = max(height[1:])
            sub_max_pos = height[1:].index(sub_max) + 1
        else:
            sub_max = max(height[:(len(height) - 1)])
            sub_max_pos = height[:len(height) - 1].index(sub_max)

        if (max_pos == 0 and len(height) - 1 > sub_max_pos > 1) or (
                max_pos == len(height) - 1 and 0 < sub_max_pos < len(height) - 2):
            if len(height[:sub_max_pos + 1]) > 2:
                tmp_trap += trap(height[:sub_max_pos + 1])
            if len(height[sub_max_pos:]) > 2:
                tmp_trap += trap(height[sub_max_pos:])
        else:
            if max_pos == 0 and sub_max_pos == 1:
                tmp_trap += trap(height[1:])
            elif max_pos == len(height) - 1 and sub_max_pos == len(height) - 2:
                tmp_trap += trap(height[:len(height) - 1])
            else:
                tmp_trap += sub_max * (len(height) - 2) - (sum(height) - max_value - sub_max)

    return tmp_trap


def test_trap():
    assert trap([0, 1, 0, 2, 1, 0, 1, 3, 2, 1, 2, 1]) == 6
    assert trap([4, 2, 0, 3, 2, 5]) == 9


if __name__ == '__main__':
    test_trap()
