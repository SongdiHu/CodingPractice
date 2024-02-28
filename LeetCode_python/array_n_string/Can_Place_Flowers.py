from typing import List


def canPlaceFlowers(flowerbed: List[int], n: int) -> bool:
    max_flower = 0

    if 1 not in flowerbed[0:2]:
        flowerbed[0] = 1
        max_flower += 1

    if 1 not in flowerbed[len(flowerbed) - 2:len(flowerbed)]:
        flowerbed[len(flowerbed) - 1] = 1
        max_flower += 1

    i = 2
    while i < len(flowerbed) - 1:
        if (flowerbed[i] == 0) and (1 not in flowerbed[i - 1:i + 2]):
            flowerbed[i] = 1
            max_flower += 1

        i = i + 1

    return n <= max_flower


def test_canPlaceFlowers():
    assert canPlaceFlowers([0, 0, 0, 0, 1], 3) is True


if __name__ == '__main__':
    test_canPlaceFlowers()
