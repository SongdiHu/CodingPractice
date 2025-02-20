#include <iostream>
#include <vector>
#include <cassert>
//#include "Merge_Sorted_Array.h"
//#include "Remove_Element.h"
//#include "Remove_Duplicates_from_Sorted_Array_II.h"
// #include "Best_Time_to_Buy_and_Sell_Stock .h"
#include "Greatest_Common_Div.h"

using namespace std;

int main(){
//     vector<int> nums1 = {2,1,2,0,1};
//     Solution xx;
//     int k = xx.maxProfit(nums1);
// //    for (int i: nums1)
// //        cout << i << ' ';
// //    cout << "\n";
//     cout << k;
    Solution xx;
    string largest_common_div = xx.gcdOfStrings("ABCABC", "ABCD");
    cout << largest_common_div << endl;
    return 0;
}