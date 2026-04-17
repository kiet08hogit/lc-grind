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
    int dfs(TreeNode * root, int& num ){
        if(root==nullptr){
            return 0;
        }
        int leftheight= dfs(root->left,num);
        int rightheight= dfs(root->right,num);
        num= max(leftheight+rightheight,num);
        return max(leftheight,rightheight)+1;
    }
    int diameterOfBinaryTree(TreeNode* root) {
       int num = 0;
       dfs(root,num);
        return num;
    }
};
