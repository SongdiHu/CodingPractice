# You are given two strings word1 and word2. Merge the strings by adding letters in alternating order,
# starting with word1. If a string is longer than the other, append the additional letters onto
# the end of the merged string.
#
# Return the merged string.

import pytest


def mergeAlternately(word1: str, word2: str) -> str:

    word3 = ""

    for i in range(min(len(word1), len(word2)) + 1):
        if i < min(len(word1), len(word2)):
            word3 += word1[i] + word2[i]
        else:
            word3 += word1[i:] if len(word1) > i else word2[i:]

    return word3


def test_mergeAlternately():
    assert mergeAlternately("abc", "pqr") == "apbqcr"
    assert mergeAlternately("ab", "pqrs") == "apbqrs"
    assert mergeAlternately("abcd", "pq") == "apbqcd"


if __name__ == "__main__":
    test_mergeAlternately()
