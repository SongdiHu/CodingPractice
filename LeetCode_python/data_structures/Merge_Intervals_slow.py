# Given an array of intervals where intervals[i] = [starti, endi], merge all overlapping intervals, and return an
# array of the non-overlapping intervals that cover all the intervals in the input.
#
# Constraints:
#
#     1 <= intervals.length <= 104
#     intervals[i].length == 2
#     0 <= starti <= endi <= 104


from typing import List


def merge(intervals: List[List[int]]) -> List[List[int]]:

    def get_first(pair):
        return pair[0]

    intervals.sort(key=get_first)

    list_all = []
    head = intervals[0][0]
    tail = intervals[0][1]

    if len(intervals) > 1:
        i = 0
        while i < len(intervals):
            if tail < intervals[i][0]:
                list_all.append([head, tail])
                head = intervals[i][0]
                tail = intervals[i][1]
            else:
                tail = max(tail, intervals[i][1])

            if i == len(intervals) - 1:
                list_all.append([head, tail])

            i += 1

        return list_all
    else:
        return intervals


def test_merge():
    assert merge([[1, 3]]) == [[1, 3]]
    assert merge([[1, 4], [0, 4]]) == [[0, 4]]
    assert merge([[1, 4], [0, 1]]) == [[0, 4]]
    assert merge([[1, 4], [0, 0]]) == [[0, 0], [1, 4]]
    assert merge([[2, 3], [4, 5], [6, 7], [8, 9], [1, 10]]) == [[1, 10]]
