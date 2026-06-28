#include <algorithm> // std::reverse, std::swap
#include <vector>

class Solution {
public:
    // [1,2]
    // [3,4]
    //   |
    //   v
    // [3, 1]
    // [4, 2]
    // matrix.size() == matrix[i].size()
    // 
    // 90 - degree clockwise roration
    // 1. transpose the matrix -> swap matrix[row][col] with matrix[col][row]
    // 2. Reverse each row -> this mvoes columns into their correct clockwise positions
    // '''
    //     [1,2,3]
    //     [4,5,6]
    //     [7,8,9]
    //         transpose
    //     [1,4,7]
    //     [2,5,8]
    //     [3,6,9]
    //         reverse each row
    //     [7,4,1]
    //     [8,5,2]
    //     [9,6,3]

    //     matrix[row][col] -> matrix[col][row]

    //     for row from 0 to n - 1:
    //         for col from row+1 to n-1
    //             swap(matrix[row][col], matrix[col][row])
            
    //     for each row:
    //         reverse(row.begin(), row.end())
    // '''
    void rotate(vector<vector<int>>& matrix) {
        int n = static_cast<int>(matrix.size());

        for(int row{0}; row < n; ++row){
            for(int col{row+1}; col < n; ++col){
                std::swap(matrix[row][col], matrix[col][row]);
            }
        }

        for (int row{0}; row < n; ++row){
            std::reverse(matrix[row].begin(), matrix[row].end());
        }
    }

    // time complexity
    // n(n-1)/2 -> O(n^2)
    // n rows * n elements per row = n^2 -> O(n^2)
    // O(n^2) + O(n^2) = O(n^2)
    // space complexity
    // O(1)
};
