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
    bool isValidBST(TreeNode* root) {
        return validhelper(root, INT_MIN, INT_MAX);
    }

    bool validhelper(TreeNode * curr, int lower, int upper){
        if(curr == nullptr) return true;
        if(curr->val <= lower || curr->val >= upper) return false;
        return validhelper(curr->right, curr->val, upper) && validhelper(curr->left, lower,curr->val);
    }
};
