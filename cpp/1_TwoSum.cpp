#include <iostream>
#include <vector>
#include <unordered_map>

class Solution {
public:
    std::vector<int> twoSum(std::vector<int>& nums, int target) {
        std::unordered_map<int, int> seen;
        std::vector<int> indices;
        int doubleValue = 0;
        for (int i = 0; i < nums.size(); ++i) {
            int num = nums[i];
            if (seen.find(target - num) != seen.end() && num == target - num) {
                doubleValue = num;
            } else if (seen.find(target - num) != seen.end() && num != target - num) {
                indices.push_back(seen[target - num]);
                indices.push_back(i);
                return indices;
            }
            seen[num] = i;
        }
        if (indices.empty()) {
            for (int i = 0; i < nums.size(); ++i) {
                if (nums[i] == doubleValue) {
                    indices.push_back(i);
                }
            }
        }
        return indices;
    }
};

int main() {
    Solution solution;
    std::vector<int> nums = {3, 3};
    auto result = solution.twoSum(nums, 6);
    for (int num : result) {
        std::cout << num << " ";
    }
    std::cout << std::endl;
    return 0;
}
