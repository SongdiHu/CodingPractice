//
// Created by gobs3 on 2024-01-08.
//

#ifndef CODINGPRACTICE_REMOVE_DUPLICATES_H
#define CODINGPRACTICE_REMOVE_DUPLICATES_H

#include <iostream>
#include <vector>

using namespace std;

class Remove_Duplicates {
public:
    int removeDuplicates_0(vector<int>& nums) {
        if (nums.empty()){
            return 0;
        }
        int i = 0;
        while(i < nums.size() - 1){
            if (nums[i] != nums[i+1]){
                i++;
            }else{
                nums.erase(nums.begin() + i);
            }
        }
        return i+1;
    }

    int removeDuplicates_1(vector<int>& nums) {
        int i = 1;
        int j = 1;
        while (j < nums.size()){
            if (nums[i-1] != nums[j]){
                nums[i] = nums[j];
                i++;
            }
            j++;
        }
        return i;
    }
};


#endif //CODINGPRACTICE_REMOVE_DUPLICATES_H
