# For two strings s and t, we say "t divides s" if and only if s = t + ... + t (i.e., t is concatenated with itself one or more times).
#
# Given two strings str1 and str2, return the largest string x such that x divides both str1 and str2.


def gcdOfStrings(str1: str, str2: str) -> str:
    def divider_check(str0, pattern):
        l_pattern = len(pattern)
        l_str = len(str0)

        if l_pattern == l_str:
            return str0 == pattern
        elif l_str % l_pattern != 0:
            return False
        else:
            i = l_pattern
            while i <= l_str:
                tmp_str = str0[(i - l_pattern):i]
                # 7 - 3 - 3
                if tmp_str != pattern:
                    return False
                i += l_pattern

        return True

    if set(str1) != set(str2):
        return ""

    if len(str1) < len(str2):
        gcd = str1
        text = str2
    else:
        gcd = str2
        text = str1

    alphabet_len = len(set(gcd))
    gcd_len = len(gcd)
    text_len = len(text)

    if gcd_len != text_len and gcd_len > text_len/2:
        gcd = gcd[:int(gcd_len/2)]

    while True:
        if not divider_check(str1, gcd) or not divider_check(str2, gcd):
            if len(gcd) <= alphabet_len:
                return ""
            else:
                gcd = gcd[:(len(gcd)-1)]
        else:
            return gcd


def test_gcdOfStrings():
    assert gcdOfStrings("AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA", "AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA") == "AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA"
    assert gcdOfStrings("ABABABAB", "ABAB") == "ABAB"
    assert gcdOfStrings("LEET", "CODE") == ""
    assert gcdOfStrings("TAUXXTAUXXTAUXXTAUXXTAUXX", "TAUXXTAUXXTAUXXTAUXXTAUXXTAUXXTAUXXTAUXXTAUXX") == "TAUXX"
    assert gcdOfStrings("ABCABCABC", "ABCAAA") == ""


# def test_divider_check():
#     assert divider_check("ABABAB", "AB") == True
#     assert divider_check("LEET", "CODE") == False
#     assert divider_check("QWERQWER", "QWER") == True


if __name__ == "__main__":
    # test_divider_check()
    test_gcdOfStrings()
