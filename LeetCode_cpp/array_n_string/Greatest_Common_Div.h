//
// Created by gobs3 on 2025-01-17.
//

#ifndef GREATEST_COMMON_DIV_H
#define GREATEST_COMMON_DIV_H
#include <numeric>

#endif //GREATEST_COMMON_DIV_H

#include <stdio.h>
#include <iostream>
#include <map>
#include <algorithm>
#include <vector>

using namespace std;

class Solution {
  public:
    string gcdOfStrings(string str1, string str2) {
        return (str1 + str2 == str2 + str1)?
        str1.substr(0, gcd(size(str1),size(str2))): "";
    }
};
