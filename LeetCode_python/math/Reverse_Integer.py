# Given a signed 32-bit integer x, return x with its digits reversed. If reversing x causes the value to go outside the signed 32-bit integer range [-231, 231 - 1], then return 0.
#
# Assume the environment does not allow you to store 64-bit integers (signed or unsigned).

def reverse(x: int) -> int:
    upper_limit = 2 ** 31 - 1
    lower_limit = -2 ** 31

    string_list_x = [a for a in str(abs(x))]
    string_reversed = ''
    for a in string_list_x:
        string_reversed = a + string_reversed

    reversed_number = int(string_reversed)
    # print(reversed_number)
    reversed_number = -reversed_number if x < 0 else reversed_number

    return reversed_number if lower_limit <= reversed_number <= upper_limit else 0


if __name__ == '__main__':
    reversed_number = reverse(1203)
    print(reversed_number)

    reversed_number = reverse(-123)
    print(reversed_number)

    reversed_number = reverse(120)
    print(reversed_number)
