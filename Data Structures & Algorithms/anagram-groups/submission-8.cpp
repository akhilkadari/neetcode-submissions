class Solution {
public:
    vector<vector<string>> groupAnagrams(vector<string>& strs) {
        unordered_map <string, vector<string>> hashMap; // hashmap initialization. string -> list of strings (vector)
        // range based loop in c++
        // : strs -> "for each element in the container strs"
        // auto -> tells the compiler "figure out the type automatically"
        // & (reference) -> s is a reference to the original string not a copy
        // without &, s is a COPY of each string
        // changes to s modifies the original
        for (const auto& s : strs){
            vector<int> count (26, 0); // initializes count as a vector with 26 zeros
            for (char c : s){
                count[c - 'a']++;
            }
            // converting the array count to a string then to use it as the key
            string key = to_string(count[0]);
            for (int i = 1; i < 26; i++){
                key += ',' + to_string(count[i]);
            }
            hashMap[key].push_back(s);
       } 
       // initialize vector of vector strings result
       // const auto& pair -> references to the key-value pair within hashMap
       vector<vector<string>> result;
       for (const auto& pair: hashMap){
            result.push_back(pair.second);
       }
       return result;
    }
};
