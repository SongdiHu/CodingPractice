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

    if len(intervals) > 1:
        head_pair = min(intervals, key=lambda x: x[0])

        list_pos = []
        for i in range(len(intervals)):
            list_pos.append([intervals[i][0], i])
            list_pos.append([intervals[i][1], i])

        list_pos.sort(key=lambda x: x[0])

        list_all = []
        list_single = []
        head = head_pair[0]
        tail = head_pair[1]

        for i in range(len(list_pos)):
            if i != 0 and not list_single and list_pos[i][0] != list_pos[i - 1][0]:
                list_all.append([head, tail])

            if list_pos[i][1] not in list_single:
                if not list_single and list_pos[i][0] != list_pos[i - 1][0]:
                    head = list_pos[i][0]
                list_single.append(list_pos[i][1])
            else:
                list_single.remove(list_pos[i][1])
                if not list_single:
                    tail = list_pos[i][0]

        list_all.append([head, tail])

        return list_all
    else:
        return intervals


def test_merge():
    assert merge([[1, 3]]) == [[1, 3]]
    assert merge([[1, 4], [0, 4]]) == [[0, 4]]
    assert merge([[1, 4], [0, 1]]) == [[0, 4]]
    assert merge([[1, 4], [0, 0]]) == [[0, 0], [1, 4]]
    assert merge([[2, 3], [4, 5], [6, 7], [8, 9], [1, 10]]) == [[1, 10]]
