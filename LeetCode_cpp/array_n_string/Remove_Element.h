//
// Created by gobs3 on 2024-01-08.
//

#ifndef CODINGPRACTICE_REMOVE_ELEMENT_H
#define CODINGPRACTICE_REMOVE_ELEMENT_H

#endif //CODINGPRACTICE_REMOVE_ELEMENT_H

#include <iostream>
#include <vector>

using namespace std;

class Remove_Element {
public:
    int removeElement_0(vector<int>& nums, int val) {
        int i = 0;
        while (i < nums.size()){
            if (nums[i] == val){
                nums.erase(nums.begin() + i);
            }else{
                i++;
            }
        }
        return i;
    }
    int removeElement_1(vector<int>& nums, int val) {
        int index = 0;

        for(int i = 0; i< nums.size(); i++){
            if(nums[i] != val){
                nums[index] = nums[i];
                index++;
            }
        }
        return index;
    }
};
