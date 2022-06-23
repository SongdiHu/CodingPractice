# Given a string s, return true if the s can be palindrome after deleting at most one character from it.
#
# Constraints:
#
#     1 <= s.length <= 105
#     s consists of lowercase English letters.


def validPalindrome(s: str) -> bool:
    s_r = s[::-1]
    if s == s_r:
        return True
    else:
        for i in range(len(s)):
            if s[i] != s_r[i]:
                s_new = s[:i]+s[i+1:]
                sr_new = s_r[:i]+s_r[i+1:]
                return (s_new == s_new[::-1]) or (sr_new == sr_new[::-1])


def test_validPalindrome():
    assert validPalindrome("lcupuufxoohdfpggpfdhooxfuupucul") is True

