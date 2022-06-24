# Given two strings s and t, return true if s is a subsequence of t, or false otherwise.
#
# A subsequence of a string is a new string that is formed from the original string by deleting some (can be none) of
# the characters without disturbing the relative positions of the remaining characters. (i.e., "ace" is a subsequence
# of "abcde" while "aec" is not).
#
# Constraints:
#
#     0 <= s.length <= 100
#     0 <= t.length <= 104
#     s and t consist only of lowercase English letters.
#
# Follow up: Suppose there are lots of incoming s, say s1, s2, ..., sk where k >= 109, and you want to check one by
# one to see if t has its subsequence. In this scenario, how would you change your code?


def isSubsequence(s: str, t: str) -> bool:
    i, j = 0, 0

    while i < len(s) and j < len(t):
        if s[i] == t[j]:
            i += 1
        j += 1

    return i == len(s)


def test_isSubsequence():
    assert isSubsequence("abc", "ahbgdc") is True
    assert isSubsequence("axc", "ahbgdc") is False
    assert isSubsequence("aaaaaa", "bbaaaa") is False


if __name__ == "__main__":
    test_isSubsequence()