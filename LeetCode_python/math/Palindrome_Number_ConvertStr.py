# Given an integer x, return true if x is palindrome integer.
#
# An integer is a palindrome when it reads the same backward as forward.
#
# For example, 121 is a palindrome while 123 or -121 is not.

def isPalindrome(self, x: int) -> bool:
    x = str(x)
    if x == x[::-1]:
        return True
    else:
        return False
