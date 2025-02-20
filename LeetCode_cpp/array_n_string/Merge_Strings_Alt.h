//
// Created by gobs3 on 2025-01-17.
//

#ifndef MERGE_STRINGS_ALT_H
#define MERGE_STRINGS_ALT_H

#endif //MERGE_STRINGS_ALT_H

#include <iostream>
#include <map>
#include <algorithm>
#include <vector>

using namespace std;

class Solution {
public:
    string mergeAlternately(string word1, string word2) {
        string result = "";
        int i = 0;
        while (i < word1.length() || i < word2.length()) {
            if (i < word1.length()) {
                result += word1[i];
            }
            if (i < word2.length()) {
                result += word2[i];
            }
            i++;
        }
        return result;
    }
};
