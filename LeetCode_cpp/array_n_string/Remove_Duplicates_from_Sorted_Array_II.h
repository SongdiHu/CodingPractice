
#ifndef CODINGPRACTICE_REMOVE_DUPLICATES_FROM_SORTED_ARRAY_II_H
#define CODINGPRACTICE_REMOVE_DUPLICATES_FROM_SORTED_ARRAY_II_H

#endif //CODINGPRACTICE_REMOVE_DUPLICATES_FROM_SORTED_ARRAY_II_H

#include <iostream>
#include <vector>

using namespace std;

class Solution {
public:
    int removeDuplicates(vector<int>& nums) {
        if (nums.size() > 2){
            int i = 2;
            while (i < nums.size()){
                if (nums[i] == nums[i-2]){
                    nums.erase(nums.begin() + i);
                }else{
                    i ++;
                }
            }
            return i;
        }else{
            return nums.size();
        }
    }
};
