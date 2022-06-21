# Roman numerals are represented by seven different symbols: I, V, X, L, C, D and M.
#
# For example, 2 is written as II in Roman numeral, just two ones added together. 12 is written as XII,
# which is simply X + II. The number 27 is written as XXVII, which is XX + V + II.
#
# Roman numerals are usually written largest to smallest from left to right. However, the numeral for four is not
# IIII. Instead, the number four is written as IV. Because the one is before the five we subtract it making four. The
# same principle applies to the number nine, which is written as IX. There are six instances where subtraction is used:
#
#     I can be placed before V (5) and X (10) to make 4 and 9.
#     X can be placed before L (50) and C (100) to make 40 and 90.
#     C can be placed before D (500) and M (1000) to make 400 and 900.
#
# Given a roman numeral, convert it to an integer.
#
# Constraints:
#
#     1 <= s.length <= 15
#     s contains only the characters ('I', 'V', 'X', 'L', 'C', 'D', 'M').
#     It is guaranteed that s is a valid roman numeral in the range [1, 3999].


def romanToInt(s: str) -> int:
    roman_dict = {"I": 1, "V": 5, "X": 10, "L": 50,
                  "C": 100, "D": 500, "M": 1000}
    special_dict = {"IV": 4, "IX": 9, "XL": 40,
                    "XC": 90, "CD": 400, "CM": 900}

    final_integer = 0
    i = 1
    while i < len(s) + 1:
        if s[i-1:i+1] in special_dict:
            final_integer += special_dict[s[i-1:i+1]]
            i += 1
        else:
            final_integer += roman_dict[s[i-1]]
        i += 1

    return final_integer


def test_romanToInt():
    assert romanToInt("I") == 1
    assert romanToInt("II") == 2
    assert romanToInt("III") == 3
    assert romanToInt("VI") == 6
    assert romanToInt("IV") == 4
    assert romanToInt("MCMXCIX") == 1999


if __name__ == "__main__":
    test_romanToInt()