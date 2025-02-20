//
// Created by gobs3 on 2025-01-19.
//

#ifndef CAN_PLACE_FLOWERS_H
#define CAN_PLACE_FLOWERS_H

#endif //CAN_PLACE_FLOWERS_H

#include <stdio.h>
#include <iostream>
#include <map>
#include <algorithm>
#include <vector>

using namespace std;

class Solution {
  public:
    bool canPlaceFlowers(vector<int>& flowerbed, int n) {
        int plantable = 0;
        for(int i = 0; i < flowerbed.size(); i++){
            bool left = i == 0 || flowerbed[i - 1] == 0;
            bool right = i == (flowerbed.size() - 1) || flowerbed[i + 1] == 0;
            if (left && right && flowerbed[i] == 0){
                flowerbed[i] = 1;
                n--;
            }
        }
        return n <= 0;
    }
};
