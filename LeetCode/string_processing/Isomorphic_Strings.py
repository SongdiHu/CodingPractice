# Given two strings s and t, determine if they are isomorphic.
#
# Two strings s and t are isomorphic if the characters in s can be replaced to get t.
#
# All occurrences of a character must be replaced with another character while preserving the order of characters. No
# two characters may map to the same character, but a character may map to itself.
#
# Constraints:
#
# 1 <= s.length <= 5 * 104
# t.length == s.length
# s and t consist of any valid ascii character.


def isIsomorphic(s: str, t: str) -> bool:
    map_dict = {}

    for ind, c in enumerate(s):
        if c not in map_dict:
            if t[ind] not in map_dict.values():
                map_dict[c] = t[ind]
            else:
                return False
        else:
            if map_dict[c] != t[ind]:
                return False

    return True


def test_isIsomorphic():
    assert isIsomorphic("egg", "add") is True
    assert isIsomorphic("foo", "bar") is False
    assert isIsomorphic("paper", "title") is True
    assert isIsomorphic("babc", "baba") is False
    assert isIsomorphic("paper", "title") is True


if __name__ == "__main__":
    test_isIsomorphic()
