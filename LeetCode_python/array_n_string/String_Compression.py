from typing import List


def compress(chars: List[str]) -> int:
    insert_pos = 0
    s = ""
    i = 1
    current_char = chars[0]
    repetition = 1
    rt_len = 1
    while i < len(chars):
        if i < len(chars) - 1:
            if chars[i] == current_char:
                repetition += 1
            else:
                s += current_char
                current_char = chars[i]
                if repetition > 1:
                    s += str(repetition)
                chars[insert_pos:(insert_pos + len(s))] = list(s)
                insert_pos = insert_pos + len(s)
                s = ""
                repetition = 1
        else:
            s += current_char
            if chars[i] == current_char:
                repetition += 1
                if repetition > 1:
                    s += str(repetition)
            else:
                if repetition > 1:
                    s += str(repetition)
                s += chars[i]
            chars[insert_pos:(insert_pos + len(s))] = list(s)
            chars[(insert_pos + len(s)):] = ["" for x in range(len(chars) - insert_pos - len(s))]
            rt_len = insert_pos + len(s)
        i += 1
    return rt_len


def test_compress():
    assert compress(["a"]) == 1
    assert compress(["a", "b", "b", "b", "b", "b", "b", "b", "b", "b", "b", "b", "b"]) == 4
    assert compress(["a", "a", "a", "b", "b", "a", "a"]) == 6
    assert compress(["a", "a", "a", "a", "a", "b"]) == 3


if __name__ == '__main__':
    test_compress()
