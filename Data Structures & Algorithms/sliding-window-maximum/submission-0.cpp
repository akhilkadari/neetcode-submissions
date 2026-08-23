class Solution {
public:
    vector<int> maxSlidingWindow(vector<int>& nums, int k) {
        vector<int> output(nums.size()-k+1);
        deque<int> q;
        int l = 0, r = 0;

        while(r < nums.size()){
            // check for values smaller than current value (nums[r]) and if values are smaller, remove
            while(!q.empty() && nums[q.back()] < nums[r]){
                q.pop_back();
            }
            // add current index
            q.push_back(r);

            // remove any out of window indices
            if(q.front( ) < l){
                q.pop_front();
            }


            if ((r+1) >= k){
                output[l] = nums[q.front()];
                l++;
            }
            r++;
        }
        return output;
    }
};
