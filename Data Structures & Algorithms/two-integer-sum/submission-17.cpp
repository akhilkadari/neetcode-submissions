class Solution {
public:
    vector<int> twoSum(vector<int>& nums, int target) {
        int n = nums.size(); // get size of vector nums
        unordered_map<int, int> hashMap; // hashmap usage in C++

        for(int i = 0; i < n; i++){
            int complement = target - nums[i];
            // find(key) -> looks for a key in a map
            // if found it returns an iterator (pointer) to that key-value pair
            // if not found it returns hashMap.end() (a special "past-the-end" marker) 
            if (hashMap.find(complement) != hashMap.end()){
                return {hashMap[complement], i};
            }
            // one way to insert key-value pairs into a hashmap
            hashMap.insert({nums[i], i});
            // or hashMap[nums[i]] = i also works
        }
        return {};
    }
};