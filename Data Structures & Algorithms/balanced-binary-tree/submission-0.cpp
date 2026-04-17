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
    bool isBalanced(TreeNode* root) {
        if (!root) return true;
        int first= getHeight( root->left);
        int second = getHeight(root->right);
        if(abs(first - second) > 1 ) return false;
        return isBalanced(root->left) && isBalanced(root->right);
    }
    int getHeight(TreeNode* curr){
        if(curr== nullptr) return 0;
        return max(getHeight(curr->left), getHeight(curr->right))+1;
    }
};
