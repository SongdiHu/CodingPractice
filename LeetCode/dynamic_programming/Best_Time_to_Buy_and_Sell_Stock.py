# You are given an array prices where prices[i] is the price of a given stock on the ith day.
#
# You want to maximize your profit by choosing a single day to buy one stock and choosing a different day in the
# future to sell that stock.
#
# Return the maximum profit you can achieve from this transaction. If you cannot achieve any profit, return 0.
#
# Constraints:
#
#     1 <= prices.length <= 105
#     0 <= prices[i] <= 104


from typing import List


def maxProfit(prices: List[int]) -> int:
    if len(prices) < 2:
        return 0
    else:
        curr_ptr, next_ptr = len(prices) - 2, len(prices) - 1
        optim_overall = 0
        optim_local = 0
        while curr_ptr >= 0:
            optim_local = max(0, prices[next_ptr] - prices[curr_ptr] + optim_local)
            optim_overall = max(optim_local, optim_overall)

            next_ptr = curr_ptr
            curr_ptr -= 1
    return optim_overall


# This is abandoned, need to copy and pass huge sub-lists to the recursive function when the input is large.
# high time-complexity O(n^2). (Memory usage will also be very inefficient -> a lot of duplicate data)

def maxProfit_rec(prices):
    if len(prices) > 2:
        optim_later, optim_overall = maxProfit_rec(prices[1:])
        optim_current = max(0, prices[1] - prices[0] + optim_later)
        return optim_current, max(optim_current, optim_overall)
    else:
        last_max = max(0, prices[1] - prices[0])
        return last_max, last_max


def test_maxProfit():
    assert maxProfit([7, 1, 5, 3, 6, 4]) == 5
