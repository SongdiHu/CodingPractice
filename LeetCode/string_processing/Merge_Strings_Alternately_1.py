# You are given two strings word1 and word2. Merge the strings by adding letters in alternating order,
# starting with word1. If a string is longer than the other, append the additional letters onto
# the end of the merged string.
#
# Return the merged string.

import pytest


def mergeAlternately(word1: str, word2: str) -> str:

    word3 = ""
    i = 0
    l1 = len(word1)
    l2 = len(word2)
    while i < min(l1, l2):
        word3 += word1[i] + word2[i]
        i += 1

    if l1 != l2:
        word3 += word1[l2:] if l1 > l2 else word2[l1:]

    return word3


def test_mergeAlternately():
    assert mergeAlternately("abc", "pqr") == "apbqcr"
    assert mergeAlternately("ab", "pqrs") == "apbqrs"
    assert mergeAlternately("abcd", "pq") == "apbqcd"


if __name__ == "__main__":
    test_mergeAlternately()
