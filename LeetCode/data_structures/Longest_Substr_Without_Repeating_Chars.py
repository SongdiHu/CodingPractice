# Given a string s, find the length of the longest substring without repeating characters.
#
# Constraints:
#
#     0 <= s.length <= 5 * 104
#     s consists of English letters, digits, symbols and spaces.


def lengthOfLongestSubstring(s: str) -> int:
    head_index = 0
    curr_length = 1
    max_length = 0
    s_length = len(s)

    if s_length > 1:
        for i in range(1, s_length):
            str_tmp = s[head_index:i]
            if s[i] not in str_tmp:
                curr_length += 1
            else:
                max_length = max(max_length, curr_length)
                head_index = str_tmp.rindex(s[i]) + head_index + 1
                curr_length = i - head_index + 1
        max_length = max(max_length, curr_length)

    else:
        max_length = s_length

    return max_length


def test_lengthOfLongestSubstring():
    assert lengthOfLongestSubstring("a") == 1
    assert lengthOfLongestSubstring("ab") == 2
    assert lengthOfLongestSubstring("abc") == 3
    assert lengthOfLongestSubstring("abcdefgh") == 8
    assert lengthOfLongestSubstring("abcabcbb") == 3
    assert lengthOfLongestSubstring("cdeaghcd") == 6
    assert lengthOfLongestSubstring("pwwkew") == 3


if __name__ == "__main__":
    test_lengthOfLongestSubstring()
