class Solution {
public:

    string encode(vector<string>& strs) {
        string s = "";
        for (int i = 0; i < strs.size(); i++){
            s += to_string(strs[i].length()) + '#' + strs[i];
        }
        return s;
    }

    vector<string> decode(string s) {
        vector<string> res = {};
        int i = 0;
        while(i < s.length()){
            int j = i;
            while (s[j] != '#'){
                j++;
            }
            int length = stoi(s.substr(i, j-i));
            i = j+1;
            res.push_back(s.substr(i, length));
            i += length;
        }
        return res;
    }
};
