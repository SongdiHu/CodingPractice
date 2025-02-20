//
// Created by gobs3 on 2025-02-20.
//

#ifndef FIND_PIVOT_INDEX_H
#define FIND_PIVOT_INDEX_H

#endif //FIND_PIVOT_INDEX_H

#include <stdio.h>
#include <iostream>
#include <map>
#include <algorithm>
#include <vector>
#include <numeric>

using namespace std;

class Solution{
  public:
    int findPivotIndex(vector<int>& nums){
        int n = nums.size();
        float sum = accumulate(nums.begin(), nums.end(), 0);
        float sum_head = 0;
        for(int i = 0; i < n; i++){
            if((sum - nums[i])/2 == sum_head){
                return i;
            }else{
                sum_head += nums[i];
            }
        }
        return -1;
    }
};
