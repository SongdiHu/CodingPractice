from typing import List


def productExceptSelf(nums: List[int]) -> List[int]:
    output_list = []
    nums_length = len(nums)
    left = [nums[0]]
    right = [nums[len(nums)-1]] # It's backward.
    for i in range(1, len(nums)):
        left.append(left[i-1] * nums[i])
        right.append(right[i-1] * nums[len(nums)-i-1])

    # print(left)
    # print(right)

    for i in range(len(nums)):
        if 0 < i < len(nums) - 1:
            output_list.append(left[i-1] * right[len(nums)-i-2])
        else:
            if i == 0:
                output_list.append(right[len(nums)-2])
            else:
                output_list.append(left[i-1])

    return output_list


def test_productExceptSelf():
    output = productExceptSelf([1, 2, 3, 4])
    print(output)


if __name__ == '__main__':
    test_productExceptSelf()
