# A phrase is a palindrome if, after converting all uppercase letters into lowercase letters and removing all
# non-alphanumeric characters, it reads the same forward and backward. Alphanumeric characters include letters and
# numbers.
#
# Given a string s, return true if it is a palindrome, or false otherwise.
#
# Constraints:
#
#     1 <= s.length <= 2 * 105
#     s consists only of printable ASCII characters.


def isPalindrome(s: str) -> bool:
    s_list = [char for char in s.lower() if char.isalpha() or char.isnumeric()]
    if s_list == s_list[::-1]:
        return True
    else:
        return False


def test_isPalindrome():
    assert isPalindrome("A man, a plan, a canal: Panama")
