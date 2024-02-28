
#ifndef CODINGPRACTICE_MERGE_SORTED_ARRAY_H
#define CODINGPRACTICE_MERGE_SORTED_ARRAY_H

#include <iostream>
#include <vector>

using namespace std;


class Merge_Sorted_Array {
    public:
        void merge(vector<int>& nums1, int m, vector<int>& nums2, int n) {
            int x = m - 1, y = n - 1, pt = m + n - 1;
            while (pt >= 0){
                if (y < 0 && x >= 0){
                    nums1[pt] = nums1[x];
                    x -= 1;
                }else if (x < 0 && y >= 0){
                    nums1[pt] = nums2[y];
                    y -= 1;
                }else if (nums1[x] <= nums2[y]){
                    nums1[pt] = nums2[y];
                    y -= 1;
                }else{
                    nums1[pt] = nums1[x];
                    x -= 1;
                }
                pt -= 1;
            }
        }
};


#endif //CODINGPRACTICE_MERGE_SORTED_ARRAY_H
