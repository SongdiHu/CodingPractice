//
// Created by gobs3 on 2024-01-08.
//

#ifndef CODINGPRACTICE_MAJORITY_ELEMENT_H
#define CODINGPRACTICE_MAJORITY_ELEMENT_H

#endif //CODINGPRACTICE_MAJORITY_ELEMENT_H

#include <iostream>
#include <map>
#include <algorithm>
#include <vector>

using namespace std;

class Solution {
public:
    int majorityElement_0(vector<int>& nums) {
        map<int, int> mp;
        int mx = 0;
        mp[mx] = 1;
        for (int num : nums){
            if (mp.find(num) != mp.end()){
                mp[num] += 1;
            }else{
                mp[num] = 1;
            }
            if (mp[num] >= mp[mx]){
                mx = num;
            }
        }
        return mx;
    }

    int majorityElement_1(vector<int>& nums) {
        sort(nums.begin(), nums.end());
        int n = nums.size();
        return nums[n/2];
    }
};