# Given a string s containing just the characters '(', ')', '{', '}', '[' and ']', determine if the input string is
# valid.
#
# An input string is valid if:
#
# Open brackets must be closed by the same type of brackets.
# Open brackets must be closed in the correct order.
#
# Constraints:
#
# 1 <= s.length <= 104
# s consists of parentheses only '()[]{}'.


def isValid(s: str) -> bool:
    left_dict = {'(': 0, '{': 0, '[': 0}
    right_dict = {')': '(', '}': '{', ']': '['}
    left_stack = []
    for c in s:
        if c in left_dict:
            left_dict[c] += 1
            left_stack.append(c)
        else:
            if left_stack and left_stack[-1] == right_dict[c]:
                left_dict[right_dict[c]] -= 1
                left_stack.pop()
            else:
                return False

    return all(value == 0 for value in left_dict.values())


def test_isValid():
    assert isValid("()") is True
    assert isValid("()()") is True
    assert isValid("(){}[]") is True
    assert isValid("())") is False
    assert isValid("(()") is False
    assert isValid("({)}") is False
    assert isValid(")()(") is False


if __name__ == "__main__":
    test_isValid()
