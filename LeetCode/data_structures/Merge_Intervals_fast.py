# Given an array of intervals where intervals[i] = [starti, endi], merge all overlapping intervals, and return an
# array of the non-overlapping intervals that cover all the intervals in the input.
#
# Constraints:
#
#     1 <= intervals.length <= 104
#     intervals[i].length == 2
#     0 <= starti <= endi <= 104


def merge(intervals):
    intervals.sort(key=lambda x: x[0])

    list_all = []

    for pair in intervals:
        if list_all and pair[0] <= list_all[-1][1]:
            list_all[-1][1] = max(list_all[-1][1], pair[1])
        else:
            list_all.append(pair)

    return list_all

def test_merge():
    assert merge([[1, 3]]) == [[1, 3]]
    assert merge([[1, 4], [0, 4]]) == [[0, 4]]
    assert merge([[1, 4], [0, 1]]) == [[0, 4]]
    assert merge([[1, 4], [0, 0]]) == [[0, 0], [1, 4]]
    assert merge([[2, 3], [4, 5], [6, 7], [8, 9], [1, 10]]) == [[1, 10]]
