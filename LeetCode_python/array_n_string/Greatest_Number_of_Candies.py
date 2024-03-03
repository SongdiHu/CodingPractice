from typing import List


def kidsWithCandies(candies: List[int], extraCandies: int) -> List[bool]:
    max_before = max(candies)
    return [True if (candy + extraCandies) >= max_before else False for candy in candies]


def test_kidsWithCandies():
    assert kidsWithCandies([2, 3, 5, 1, 3], 3)


if __name__ == '__main__':
    test_kidsWithCandies()
