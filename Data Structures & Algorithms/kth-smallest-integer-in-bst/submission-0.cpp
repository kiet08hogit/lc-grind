/**
 * Definition for a binary tree node.
 * struct TreeNode {
 *     int val;
 *     TreeNode *left;
 *     TreeNode *right;
 *     TreeNode() : val(0), left(nullptr), right(nullptr) {}
 *     TreeNode(int x) : val(x), left(nullptr), right(nullptr) {}
 *     TreeNode(int x, TreeNode *left, TreeNode *right) : val(x), left(left), right(right) {}
 * };
 */

class Solution {
public:
    void dfs(TreeNode * curr, int k, vector<int> & arr){   
        if(!curr) return;    
        dfs(curr->left,k,arr);
        arr.push_back(curr->val);
        dfs(curr->right,k,arr);
    }
    int kthSmallest(TreeNode* root, int k) {
        int count = 0;
        vector <int> arr;
        dfs(root, k , arr);
        return arr[k-1];
    }
};
