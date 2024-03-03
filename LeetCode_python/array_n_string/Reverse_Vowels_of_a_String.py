def reverseVowels(s: str) -> str:
    vowels = ['a', 'e', 'i', 'o', 'u',
              'A', 'E', 'I', 'O', 'U']
    s = list(s)
    i = 0
    j = len(s) - 1
    while i < j:
        if s[i] not in vowels:
            i += 1
        if s[j] not in vowels:
            j -= 1
        if s[i] in vowels and s[j] in vowels:
            if s[i] != s[j]:
                c_tmp = s[i]
                s[i] = s[j]
                s[j] = c_tmp
            i += 1
            j -= 1

    return "".join(s)


def test_reverseVowels():
    assert reverseVowels("leetcode") == "leotcede"


if __name__ == '__main__':
    test_reverseVowels()
