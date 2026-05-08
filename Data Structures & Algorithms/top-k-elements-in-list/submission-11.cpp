class Solution {
public:
    vector<int> topKFrequent(vector<int>& nums, int k) {
        // initialize a hashmap to store frequencies
        unordered_map<int, int> count;
        for(int num: nums){
            count[num]++;
        }

        // priority_queue template in c++
        // - pair <int, int>: type of element it will store
        // - vector<pair<int, int>>: priority queue doesn't store elements in a special way
        //    so you must specify which container to use
        // - greater<pair<int, int>> is a built in c++ comparison function 
        //    that says the smaller the pair the higher priority it gets
        priority_queue<pair<int, int>, vector<pair<int, int>>, greater<pair<int, int>>> heap;
        for (auto& entry : count){
            heap.push({-entry.second, entry.first});
            // if (heap.size() > k){
            //     heap.pop();
            // }
        }

        vector<int> res;
        for(int i = 0; i < k; i++){
            res.push_back(heap.top().second);
            heap.pop();
        }
        return res;

    }   
};
