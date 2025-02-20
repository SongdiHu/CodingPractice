//
// Created by gobs3 on 2025-01-17.
//

#ifndef KIDS_GREATEST_CANDIES_H
#define KIDS_GREATEST_CANDIES_H

#endif //KIDS_GREATEST_CANDIES_H

#include <stdio.h>
#include <iostream>
#include <map>
#include <algorithm>
#include <vector>

using namespace std;

class Solution {
public:
    vector<bool> kidsWithCandies(vector<int>& candies, int extraCandies) {
        int maxCandies = 0;
        for (int candy: candies){
          maxCandies = max(maxCandies, candy);
        }
        vector<bool> result;
        for (int candy: candies){
          result.push_back(candy + extraCandies >= maxCandies);
        }
        return result;
    }
};
