//
// Created by gobs3 on 2024-01-08.
//

#ifndef CODINGPRACTICE_BEST_TIME_TO_BUY_AND_SELL_STOCK_H
#define CODINGPRACTICE_BEST_TIME_TO_BUY_AND_SELL_STOCK_H

#endif //CODINGPRACTICE_BEST_TIME_TO_BUY_AND_SELL_STOCK_H

#include <iostream>
#include <map>
#include "algorithm"
#include <vector>
using namespace std;

class Solution {
public:
    int maxProfit(vector<int>& prices) {
        int best_profit = 0;
        int prev_minimum = prices[0];
        for (int i = 1; i < prices.size(); i++){
            int tmp_profit = prices[i] - prev_minimum;
            if (tmp_profit > best_profit){
                best_profit = tmp_profit;
            }
            if (prices[i] < prev_minimum){
                prev_minimum = prices[i];
            }
        }
        return best_profit;
    }
};
